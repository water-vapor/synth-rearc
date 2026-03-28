from .generator import generate_782b5218
from .verifier import verify_782b5218


TASK_ID = "782b5218"
generate = generate_782b5218
verify = verify_782b5218
REFERENCE_TASK_PATH = "data/official/arc2/training/782b5218.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_782b5218",
    "verify",
    "verify_782b5218",
]
