from .generator import generate_60c09cac
from .verifier import verify_60c09cac


TASK_ID = "60c09cac"
generate = generate_60c09cac
verify = verify_60c09cac
REFERENCE_TASK_PATH = "data/official/arc2/training/60c09cac.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_60c09cac",
    "verify",
    "verify_60c09cac",
]
