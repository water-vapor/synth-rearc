from .generator import generate_b457fec5
from .verifier import verify_b457fec5


TASK_ID = "b457fec5"
generate = generate_b457fec5
verify = verify_b457fec5
REFERENCE_TASK_PATH = "data/official/arc2/training/b457fec5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b457fec5",
    "verify",
    "verify_b457fec5",
]
