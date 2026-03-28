from .generator import generate_62b74c02
from .verifier import verify_62b74c02


TASK_ID = "62b74c02"
generate = generate_62b74c02
verify = verify_62b74c02
REFERENCE_TASK_PATH = "data/official/arc2/training/62b74c02.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_62b74c02",
    "verify",
    "verify_62b74c02",
]
