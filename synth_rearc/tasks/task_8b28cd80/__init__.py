from .generator import generate_8b28cd80
from .verifier import verify_8b28cd80


TASK_ID = "8b28cd80"
generate = generate_8b28cd80
verify = verify_8b28cd80
REFERENCE_TASK_PATH = "data/official/arc2/training/8b28cd80.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8b28cd80",
    "verify",
    "verify_8b28cd80",
]
