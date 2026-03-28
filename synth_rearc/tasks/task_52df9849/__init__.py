from .generator import generate_52df9849
from .verifier import verify_52df9849


TASK_ID = "52df9849"
generate = generate_52df9849
verify = verify_52df9849
REFERENCE_TASK_PATH = "data/official/arc2/training/52df9849.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_52df9849",
    "verify",
    "verify_52df9849",
]
