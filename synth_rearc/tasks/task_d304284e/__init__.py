from .generator import generate_d304284e
from .verifier import verify_d304284e


TASK_ID = "d304284e"
generate = generate_d304284e
verify = verify_d304284e
REFERENCE_TASK_PATH = "data/official/arc2/training/d304284e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d304284e",
    "verify",
    "verify_d304284e",
]
