from .generator import generate_e66aafb8
from .verifier import verify_e66aafb8


TASK_ID = "e66aafb8"
generate = generate_e66aafb8
verify = verify_e66aafb8
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/e66aafb8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e66aafb8",
    "verify",
    "verify_e66aafb8",
]
