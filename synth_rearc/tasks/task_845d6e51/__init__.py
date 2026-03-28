from .generator import generate_845d6e51
from .verifier import verify_845d6e51


TASK_ID = "845d6e51"
generate = generate_845d6e51
verify = verify_845d6e51
REFERENCE_TASK_PATH = "data/official/arc2/training/845d6e51.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_845d6e51",
    "verify",
    "verify_845d6e51",
]
