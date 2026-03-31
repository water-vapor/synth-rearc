from .generator import generate_a25697e4
from .verifier import verify_a25697e4


TASK_ID = "a25697e4"
generate = generate_a25697e4
verify = verify_a25697e4
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/a25697e4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a25697e4",
    "verify",
    "verify_a25697e4",
]
