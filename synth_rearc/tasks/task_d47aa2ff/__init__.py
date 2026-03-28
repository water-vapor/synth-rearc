from .generator import generate_d47aa2ff
from .verifier import verify_d47aa2ff


TASK_ID = "d47aa2ff"
generate = generate_d47aa2ff
verify = verify_d47aa2ff
REFERENCE_TASK_PATH = "data/official/arc2/training/d47aa2ff.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d47aa2ff",
    "verify",
    "verify_d47aa2ff",
]
