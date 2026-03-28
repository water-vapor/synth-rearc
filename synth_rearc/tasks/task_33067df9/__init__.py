from .generator import generate_33067df9
from .verifier import verify_33067df9


TASK_ID = "33067df9"
generate = generate_33067df9
verify = verify_33067df9
REFERENCE_TASK_PATH = "data/official/arc2/training/33067df9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_33067df9",
    "verify",
    "verify_33067df9",
]
