from .generator import generate_15663ba9
from .verifier import verify_15663ba9


TASK_ID = "15663ba9"
generate = generate_15663ba9
verify = verify_15663ba9
REFERENCE_TASK_PATH = "data/official/arc2/training/15663ba9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_15663ba9",
    "verify",
    "verify_15663ba9",
]
