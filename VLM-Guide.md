# VLM Serving with vLLM (Advanced Configuration)

This document provides commands to serve various Vision-Language Models (VLMs) using vLLM with advanced configurations.

## Prerequisites

1. Install vLLM with additional dependencies:
```bash
pip install vllm bitsandbytes torchvision Pillow
```
2. Launch vLLM 
```bash
CUDA_VISIBLE_DEVICES=0 vllm serve MODEL \
    --host 0.0.0.0 \
    --port PORT \
    --max-model-len MAX_SEQ_LENGTH \
    --api-key YOUR_API_KEY \
    --gpu-memory-utilization=FRAC_OF_VRAM \
    --tensor-parallel-size 1 \
    --trust-remote-code
```


## Client Example

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:50032/v1",  # Qwen2.5-VL endpoint
    api_key="YOUR_API_KEY"
)

response = client.chat.completions.create(
    model="Qwen2.5-VL-3B-Instruct",
    messages=[{
        "role": "user", 
        "content": "Analyze this image and explain the key elements..."
    }],
    max_tokens=512
)
print(response.choices[0].message.content)
```


## Models to test
1. unsloth/gemma-3n-E4B-it-unsloth-bnb-4bit
2. unsloth/gemma-3-12b-it-unsloth-bnb-4bit
3. unsloth/Llama-3.2-11B-Vision-Instruct-bnb-4bit
4. unsloth/Pixtral-12B-2409-bnb-4bit
5. unsloth/Qwen2.5-VL-7B-Instruct-unsloth-bnb-4bit
6. wnma3mz/Janus-Pro-7B-4bit
7. HuggingFaceTB/SmolVLM2-2.2B-Instruct
8. unsloth/aya-vision-8b-unsloth-bnb-4bit



