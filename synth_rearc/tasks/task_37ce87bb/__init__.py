from .generator import generate_37ce87bb
from .verifier import verify_37ce87bb


TASK_ID = "37ce87bb"
generate = generate_37ce87bb
verify = verify_37ce87bb
REFERENCE_TASK_PATH = "data/official/arc2/training/37ce87bb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_37ce87bb",
    "verify",
    "verify_37ce87bb",
]
