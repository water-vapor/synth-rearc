from .generator import generate_7e0986d6
from .verifier import verify_7e0986d6


TASK_ID = "7e0986d6"
REFERENCE_TASK_PATH = "data/official/arc1/training/7e0986d6.json"

generate = generate_7e0986d6
verify = verify_7e0986d6

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7e0986d6",
    "verify",
    "verify_7e0986d6",
]
