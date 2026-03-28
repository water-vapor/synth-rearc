from .generator import generate_bd14c3bf
from .verifier import verify_bd14c3bf


TASK_ID = "bd14c3bf"
generate = generate_bd14c3bf
verify = verify_bd14c3bf
REFERENCE_TASK_PATH = "data/official/arc2/training/bd14c3bf.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bd14c3bf",
    "verify",
    "verify_bd14c3bf",
]
