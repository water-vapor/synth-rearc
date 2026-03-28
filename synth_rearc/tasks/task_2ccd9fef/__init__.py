from .generator import generate_2ccd9fef
from .verifier import verify_2ccd9fef


TASK_ID = "2ccd9fef"
generate = generate_2ccd9fef
verify = verify_2ccd9fef
REFERENCE_TASK_PATH = "data/official/arc2/training/2ccd9fef.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2ccd9fef",
    "verify",
    "verify_2ccd9fef",
]
