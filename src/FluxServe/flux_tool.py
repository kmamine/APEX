# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from diffusers import FluxKontextPipeline
from diffusers.utils import load_image
from PIL import Image
import io
import base64

app = FastAPI(
    title="FluxKontext Image Generation API",
    description="API for generating images with FluxKontextPipeline",
    version="0.0.1"
)

# Load the model globally when the application starts
# This ensures it's loaded only once and is ready for all requests.
try:
    pipe = FluxKontextPipeline.from_pretrained("black-forest-labs/FLUX.1-Kontext-dev", torch_dtype=torch.bfloat16)
    pipe.to("cuda")
    print("FluxKontextPipeline loaded successfully.")
except Exception as e:
    print(f"Error loading FluxKontextPipeline: {e}")
    # Depending on your deployment strategy, you might want to exit or handle this more gracefully.
    pipe = None # Indicate that the pipe couldn't be loaded

class ImageGenerationRequest(BaseModel):
    input_image_base64: str  # Base64 encoded input image
    prompt: str
    guidance_scale: float = 2.5 # Default value

class ImageGenerationResponse(BaseModel):
    generated_image_base64: str

@app.post("/generate_image", response_model=ImageGenerationResponse)
async def generate_image(request: ImageGenerationRequest):
    if pipe is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Server is not ready.")

    try:
        # Decode the base64 input image
        image_bytes = base64.b64decode(request.input_image_base64)
        input_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # Perform inference
        # In a real-world scenario with long-running models,
        # you might want to offload this to a background task or a separate worker.
        # For this example, we'll run it directly.
        generated_images = pipe(
            image=input_image,
            prompt=request.prompt,
            guidance_scale=request.guidance_scale
        ).images

        if not generated_images:
            raise HTTPException(status_code=500, detail="Image generation failed: No image returned.")

        generated_image = generated_images[0]

        # Encode the generated image to base64
        buffered = io.BytesIO()
        generated_image.save(buffered, format="PNG") # You can choose other formats like JPEG
        generated_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return ImageGenerationResponse(generated_image_base64=generated_image_base64)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation error: {e}")

@app.get("/")
async def root():
    return {"message": "FluxKontext Image Generation API is running. Use /generate_image for inference."}

# To run this application:
# 1. Save the code above as `app.py`.
# 2. Install necessary libraries: `pip install fastapi uvicorn torch diffusers transformers accelerate`
#    (You'll need a CUDA-enabled PyTorch installation for GPU inference.)
# 3. Run the server: `uvicorn app:app --host 0.0.0.0 --port 8000`