from .generator import generate_46c35fc7
from .verifier import verify_46c35fc7


TASK_ID = "46c35fc7"
REFERENCE_TASK_PATH = "data/official/arc2/training/46c35fc7.json"

generate = generate_46c35fc7
verify = verify_46c35fc7

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_46c35fc7",
    "verify",
    "verify_46c35fc7",
]
