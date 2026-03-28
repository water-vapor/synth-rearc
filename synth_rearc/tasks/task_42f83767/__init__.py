from .generator import generate_42f83767
from .verifier import verify_42f83767


TASK_ID = "42f83767"
generate = generate_42f83767
verify = verify_42f83767
REFERENCE_TASK_PATH = "data/official/arc2/training/42f83767.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_42f83767",
    "verify",
    "verify_42f83767",
]
