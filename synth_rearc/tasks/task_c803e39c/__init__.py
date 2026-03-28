from .generator import generate_c803e39c
from .verifier import verify_c803e39c


TASK_ID = "c803e39c"
generate = generate_c803e39c
verify = verify_c803e39c
REFERENCE_TASK_PATH = "data/official/arc2/training/c803e39c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c803e39c",
    "verify",
    "verify_c803e39c",
]
