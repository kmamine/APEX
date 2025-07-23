CUDA_VISIBLE_DEVICES=0 vllm serve MODEL \
    --host 0.0.0.0 \
    --port PORT \
    --max-model-len MAX_SEQ_LENGTH \
    --api-key YOUR_API_KEY \
    --gpu-memory-utilization=FRAC_OF_VRAM \
    --tensor-parallel-size 1 \
    --trust-remote-code