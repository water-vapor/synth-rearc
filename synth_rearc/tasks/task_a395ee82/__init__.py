from .generator import generate_a395ee82
from .verifier import verify_a395ee82


TASK_ID = "a395ee82"
generate = generate_a395ee82
verify = verify_a395ee82
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/a395ee82.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a395ee82",
    "verify",
    "verify_a395ee82",
]
