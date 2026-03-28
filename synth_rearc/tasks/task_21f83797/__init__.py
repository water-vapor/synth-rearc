from .generator import generate_21f83797
from .verifier import verify_21f83797


TASK_ID = "21f83797"
generate = generate_21f83797
verify = verify_21f83797
REFERENCE_TASK_PATH = "data/official/arc2/training/21f83797.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_21f83797",
    "verify",
    "verify_21f83797",
]
