from .generator import generate_99caaf76
from .verifier import verify_99caaf76


TASK_ID = "99caaf76"
generate = generate_99caaf76
verify = verify_99caaf76
REFERENCE_TASK_PATH = "data/official/arc2/training/99caaf76.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_99caaf76",
    "verify",
    "verify_99caaf76",
]
