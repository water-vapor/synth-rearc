from .generator import generate_506d28a5
from .verifier import verify_506d28a5


TASK_ID = "506d28a5"
generate = generate_506d28a5
verify = verify_506d28a5
REFERENCE_TASK_PATH = "data/official/arc2/training/506d28a5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_506d28a5",
    "verify",
    "verify_506d28a5",
]
