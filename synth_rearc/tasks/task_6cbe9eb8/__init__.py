from .generator import generate_6cbe9eb8
from .verifier import verify_6cbe9eb8


TASK_ID = "6cbe9eb8"
REFERENCE_TASK_PATH = "data/official/arc2/training/6cbe9eb8.json"

generate = generate_6cbe9eb8
verify = verify_6cbe9eb8

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6cbe9eb8",
    "verify",
    "verify_6cbe9eb8",
]
