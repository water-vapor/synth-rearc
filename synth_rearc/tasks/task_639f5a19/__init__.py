from .generator import generate_639f5a19
from .verifier import verify_639f5a19


TASK_ID = "639f5a19"
generate = generate_639f5a19
verify = verify_639f5a19
REFERENCE_TASK_PATH = "data/official/arc2/training/639f5a19.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_639f5a19",
    "verify",
    "verify_639f5a19",
]
