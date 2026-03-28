from .generator import generate_b745798f
from .verifier import verify_b745798f


TASK_ID = "b745798f"
generate = generate_b745798f
verify = verify_b745798f
REFERENCE_TASK_PATH = "data/official/arc2/training/b745798f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b745798f",
    "verify",
    "verify_b745798f",
]
