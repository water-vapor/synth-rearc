from .generator import generate_2753e76c
from .verifier import verify_2753e76c


TASK_ID = "2753e76c"
REFERENCE_TASK_PATH = "data/official/arc2/training/2753e76c.json"

generate = generate_2753e76c
verify = verify_2753e76c

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2753e76c",
    "verify",
    "verify_2753e76c",
]
