from .generator import generate_800d221b
from .verifier import verify_800d221b


TASK_ID = "800d221b"
generate = generate_800d221b
verify = verify_800d221b
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/800d221b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_800d221b",
    "verify",
    "verify_800d221b",
]
