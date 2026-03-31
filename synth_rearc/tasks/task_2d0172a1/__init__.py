from .generator import generate_2d0172a1
from .verifier import verify_2d0172a1


TASK_ID = "2d0172a1"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/2d0172a1.json"

generate = generate_2d0172a1
verify = verify_2d0172a1

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2d0172a1",
    "verify",
    "verify_2d0172a1",
]
