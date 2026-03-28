from .generator import generate_c8b7cc0f
from .verifier import verify_c8b7cc0f


TASK_ID = "c8b7cc0f"
generate = generate_c8b7cc0f
verify = verify_c8b7cc0f
REFERENCE_TASK_PATH = "data/official/arc2/training/c8b7cc0f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c8b7cc0f",
    "verify",
    "verify_c8b7cc0f",
]
