from .generator import generate_afe3afe9
from .verifier import verify_afe3afe9


TASK_ID = "afe3afe9"
generate = generate_afe3afe9
verify = verify_afe3afe9
REFERENCE_TASK_PATH = "data/official/arc2/training/afe3afe9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_afe3afe9",
    "verify",
    "verify_afe3afe9",
]
