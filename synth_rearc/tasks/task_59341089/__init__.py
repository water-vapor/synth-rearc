from .generator import generate_59341089
from .verifier import verify_59341089


TASK_ID = "59341089"
generate = generate_59341089
verify = verify_59341089
REFERENCE_TASK_PATH = "data/official/arc2/training/59341089.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_59341089",
    "verify",
    "verify_59341089",
]
