from .generator import generate_ca8de6ea
from .verifier import verify_ca8de6ea


TASK_ID = "ca8de6ea"
generate = generate_ca8de6ea
verify = verify_ca8de6ea
REFERENCE_TASK_PATH = "data/official/arc2/training/ca8de6ea.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ca8de6ea",
    "verify",
    "verify_ca8de6ea",
]
