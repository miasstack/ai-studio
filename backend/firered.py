"""
FireRed Image Edit 1.1 — native diffusers inference module.
Runs alongside ComfyUI as a separate backend for Qwen-based image editing.

Model: FireRedTeam/FireRed-Image-Edit-1.1
Architecture: QwenImageEditPlusPipeline (Qwen2-VL based)
Usage: provide an input image + natural language edit instruction
"""

import base64
import io
import os
import random
import threading

import torch
from PIL import Image

# Global pipe instance — loaded lazily on first use
_pipe = None
_pipe_lock = threading.Lock()

MODEL_ID       = os.getenv("FIRERED_MODEL_ID",       "FireRedTeam/FireRed-Image-Edit-1.1")
TRANSFORMER_ID = os.getenv("FIRERED_TRANSFORMER_ID", "prithivMLmods/Qwen-Image-Edit-Rapid-AIO-V19")
HF_TOKEN       = os.getenv("HF_TOKEN", "") or None


def _load_pipe():
    global _pipe
    if _pipe is not None:
        return _pipe

    with _pipe_lock:
        if _pipe is not None:
            return _pipe

        print(f"Loading FireRed pipeline from {MODEL_ID}…")
        try:
            from diffusers import QwenImageEditPlusPipeline, FlowMatchEulerDiscreteScheduler

            try:
                from diffusers.models.attention_processor import QwenDoubleStreamAttnProcessorFA3
                attn_processor = QwenDoubleStreamAttnProcessorFA3()
            except ImportError:
                attn_processor = None

            pipe = QwenImageEditPlusPipeline.from_pretrained(
                MODEL_ID,
                torch_dtype=torch.bfloat16,
                device_map="cuda",
                token=HF_TOKEN,
            )

            if attn_processor is not None:
                try:
                    pipe.transformer.set_attn_processor(attn_processor)
                except Exception:
                    pass  # Flash Attention 3 not available — use default

            _pipe = pipe
            print("FireRed pipeline loaded.")
        except Exception as e:
            print(f"FireRed load error: {e}")
            raise

    return _pipe


def is_available() -> bool:
    """Return True if CUDA is available (FireRed requires GPU)."""
    return torch.cuda.is_available()


def decode_b64_image(b64_str: str) -> Image.Image:
    img_bytes = base64.b64decode(b64_str)
    return Image.open(io.BytesIO(img_bytes)).convert("RGB")


def encode_pil_b64(img: Image.Image, fmt: str = "PNG") -> str:
    buf = io.BytesIO()
    img.save(buf, format=fmt)
    return base64.b64encode(buf.getvalue()).decode()


def infer(
    image_b64: str,
    prompt: str,
    negative_prompt: str = "deformed, blurry, bad anatomy, bad composition, noisy",
    steps: int = 4,
    guidance: float = 1.0,
    seed: int = -1,
) -> dict:
    """
    Run FireRed image edit inference.

    Returns:
        {"image_b64": str, "seed": int}
    """
    if seed == -1:
        seed = random.randint(0, 2**32 - 1)

    pipe = _load_pipe()
    input_image = decode_b64_image(image_b64)

    # Auto-size: round to nearest 8px, preserve aspect ratio
    w, h = input_image.size
    w = round(w / 8) * 8
    h = round(h / 8) * 8
    input_image = input_image.resize((w, h), Image.LANCZOS)

    generator = torch.Generator("cuda").manual_seed(seed)

    with torch.inference_mode():
        result = pipe(
            image=input_image,
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            true_cfg_scale=guidance,
            height=h,
            width=w,
            generator=generator,
        )

    output_image = result.images[0]
    return {
        "image_b64": encode_pil_b64(output_image),
        "seed": seed,
        "width": w,
        "height": h,
    }


def unload():
    """Free GPU memory."""
    global _pipe
    with _pipe_lock:
        if _pipe is not None:
            del _pipe
            _pipe = None
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
