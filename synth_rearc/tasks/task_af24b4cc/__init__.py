from .generator import generate_af24b4cc
from .verifier import verify_af24b4cc


TASK_ID = "af24b4cc"
generate = generate_af24b4cc
verify = verify_af24b4cc
REFERENCE_TASK_PATH = "data/official/arc2/training/af24b4cc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_af24b4cc",
    "verify",
    "verify_af24b4cc",
]
