from .generator import generate_16b78196
from .verifier import verify_16b78196


TASK_ID = "16b78196"
generate = generate_16b78196
verify = verify_16b78196
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/16b78196.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_16b78196",
    "verify",
    "verify_16b78196",
]
