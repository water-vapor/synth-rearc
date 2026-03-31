from .generator import generate_88bcf3b4
from .verifier import verify_88bcf3b4


TASK_ID = "88bcf3b4"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/88bcf3b4.json"

generate = generate_88bcf3b4
verify = verify_88bcf3b4

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_88bcf3b4",
    "verify",
    "verify_88bcf3b4",
]
