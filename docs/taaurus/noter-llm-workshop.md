## LoRa

LoRa - 10x mindre compute cost ift full fine-tuning

- Paramater reduction
- GPU memory reduction (3 times less VRAM)
- Storage reduction (checkpoint size from 350GB tot 35mb)

https://github.com/HichamAgueny/llm-hpc-course/blob/main/llm_part_1.pdf

- High accuracy compared with full fine-tuning

## Quantization

What is Quantization ?
• Quantization is the process of converting a model’s numbers (weights and activations) from a high-precision
 format e.g BF16/FP16 or FP32 into a lower-precision format, typically 8-bit or 4-bit.
• Ex. In FP16: 1.23456 —>1.23 (FP8) or 123(INT8)
If 10B model is stored in FP16/BF16, each parameter occupies 2 bytes ~20 GB (10B parameters * 2 bytes/parameter).By quantizing the model to FP8, the memory required for the model weights is reduced to ~10GB.
• Quantize the model’s weights to reduce its memory footprint (VRAM).
• Quantizing the model’s intermediate activations (compute) can further enhance inference speed.
• Lower hardware cost



## vLLM

