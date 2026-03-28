from .generator import generate_c920a713
from .verifier import verify_c920a713


TASK_ID = "c920a713"
generate = generate_c920a713
verify = verify_c920a713
REFERENCE_TASK_PATH = "data/official/arc2/training/c920a713.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c920a713",
    "verify",
    "verify_c920a713",
]
