from .generator import generate_bf32578f
from .verifier import verify_bf32578f


TASK_ID = "bf32578f"
generate = generate_bf32578f
verify = verify_bf32578f
REFERENCE_TASK_PATH = "data/official/arc2/training/bf32578f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bf32578f",
    "verify",
    "verify_bf32578f",
]
