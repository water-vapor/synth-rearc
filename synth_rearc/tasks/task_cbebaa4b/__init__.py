from .generator import generate_cbebaa4b
from .verifier import verify_cbebaa4b


TASK_ID = "cbebaa4b"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/cbebaa4b.json"

generate = generate_cbebaa4b
verify = verify_cbebaa4b

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_cbebaa4b",
    "verify",
    "verify_cbebaa4b",
]
