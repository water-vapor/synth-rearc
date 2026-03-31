from .generator import generate_28a6681f
from .verifier import verify_28a6681f


TASK_ID = "28a6681f"
generate = generate_28a6681f
verify = verify_28a6681f
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/28a6681f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_28a6681f",
    "verify",
    "verify_28a6681f",
]
