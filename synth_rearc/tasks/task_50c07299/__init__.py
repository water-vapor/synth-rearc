from .generator import generate_50c07299
from .verifier import verify_50c07299


TASK_ID = "50c07299"
generate = generate_50c07299
verify = verify_50c07299
REFERENCE_TASK_PATH = "data/official/arc2/training/50c07299.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_50c07299",
    "verify",
    "verify_50c07299",
]
