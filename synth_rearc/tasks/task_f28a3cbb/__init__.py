from .generator import generate_f28a3cbb
from .verifier import verify_f28a3cbb


TASK_ID = "f28a3cbb"
generate = generate_f28a3cbb
verify = verify_f28a3cbb
REFERENCE_TASK_PATH = "data/official/arc2/training/f28a3cbb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f28a3cbb",
    "verify",
    "verify_f28a3cbb",
]
