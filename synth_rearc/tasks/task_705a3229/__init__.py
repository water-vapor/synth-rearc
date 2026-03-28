from .generator import generate_705a3229
from .verifier import verify_705a3229


TASK_ID = "705a3229"
generate = generate_705a3229
verify = verify_705a3229
REFERENCE_TASK_PATH = "data/official/arc2/training/705a3229.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_705a3229",
    "verify",
    "verify_705a3229",
]
