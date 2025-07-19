
# vllm serve a multimodal LLM model 
# This script is used to serve a multimodal LLM model using vLLM.
# It sets up the environment and starts the vLLM server with specified parameters.
#!/bin/bash



vllm serve \
    --model-path /path/to/your/multimodal_model \
    --port 8000 \
    --tensor-parallel-size 1 \
    --max-batch-size 8 \
    --max-model-len 2048 \
    --max-input-len 512 \
    --max-output-len 512 \
    --num-gpus 1 \

