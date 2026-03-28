from .generator import generate_54dc2872
from .verifier import verify_54dc2872


TASK_ID = "54dc2872"
generate = generate_54dc2872
verify = verify_54dc2872
REFERENCE_TASK_PATH = "data/official/arc2/training/54dc2872.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_54dc2872",
    "verify",
    "verify_54dc2872",
]
