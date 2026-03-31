from .generator import generate_c663677b
from .verifier import verify_c663677b


TASK_ID = "c663677b"
generate = generate_c663677b
verify = verify_c663677b
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/c663677b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c663677b",
    "verify",
    "verify_c663677b",
]
