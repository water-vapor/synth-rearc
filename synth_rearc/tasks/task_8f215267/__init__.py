from .generator import generate_8f215267
from .verifier import verify_8f215267


TASK_ID = "8f215267"
generate = generate_8f215267
verify = verify_8f215267
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/8f215267.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8f215267",
    "verify",
    "verify_8f215267",
]
