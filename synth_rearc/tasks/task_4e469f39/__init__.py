from .generator import generate_4e469f39
from .verifier import verify_4e469f39


TASK_ID = "4e469f39"
generate = generate_4e469f39
verify = verify_4e469f39
REFERENCE_TASK_PATH = "data/official/arc2/training/4e469f39.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4e469f39",
    "verify",
    "verify_4e469f39",
]
