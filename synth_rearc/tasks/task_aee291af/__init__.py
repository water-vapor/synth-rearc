from .generator import generate_aee291af
from .verifier import verify_aee291af


TASK_ID = "aee291af"
generate = generate_aee291af
verify = verify_aee291af
REFERENCE_TASK_PATH = "data/official/arc2/training/aee291af.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_aee291af",
    "verify",
    "verify_aee291af",
]
