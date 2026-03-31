from .generator import generate_8b7bacbf
from .verifier import verify_8b7bacbf


TASK_ID = "8b7bacbf"
generate = generate_8b7bacbf
verify = verify_8b7bacbf
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/8b7bacbf.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8b7bacbf",
    "verify",
    "verify_8b7bacbf",
]
