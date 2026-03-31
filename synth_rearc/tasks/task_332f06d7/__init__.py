from .generator import generate_332f06d7
from .verifier import verify_332f06d7


TASK_ID = "332f06d7"
generate = generate_332f06d7
verify = verify_332f06d7
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/332f06d7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_332f06d7",
    "verify",
    "verify_332f06d7",
]
