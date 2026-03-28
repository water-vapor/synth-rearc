from .generator import generate_0934a4d8
from .verifier import verify_0934a4d8


TASK_ID = "0934a4d8"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/0934a4d8.json"

generate = generate_0934a4d8
verify = verify_0934a4d8

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0934a4d8",
    "verify",
    "verify_0934a4d8",
]
