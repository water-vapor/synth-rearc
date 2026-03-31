from .generator import generate_47996f11
from .verifier import verify_47996f11


TASK_ID = "47996f11"
generate = generate_47996f11
verify = verify_47996f11
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/47996f11.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_47996f11",
    "verify",
    "verify_47996f11",
]
