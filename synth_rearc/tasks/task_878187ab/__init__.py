from .generator import generate_878187ab
from .verifier import verify_878187ab


TASK_ID = "878187ab"
generate = generate_878187ab
verify = verify_878187ab
REFERENCE_TASK_PATH = "data/official/arc2/training/878187ab.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_878187ab",
    "verify",
    "verify_878187ab",
]
