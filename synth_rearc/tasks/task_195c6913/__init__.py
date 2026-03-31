from .generator import generate_195c6913
from .verifier import verify_195c6913


TASK_ID = "195c6913"
generate = generate_195c6913
verify = verify_195c6913
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/195c6913.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_195c6913",
    "verify",
    "verify_195c6913",
]
