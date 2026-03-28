from .generator import generate_62ab2642
from .verifier import verify_62ab2642


TASK_ID = "62ab2642"
generate = generate_62ab2642
verify = verify_62ab2642
REFERENCE_TASK_PATH = "data/official/arc2/training/62ab2642.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_62ab2642",
    "verify",
    "verify_62ab2642",
]
