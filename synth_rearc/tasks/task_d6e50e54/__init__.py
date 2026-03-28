from .generator import generate_d6e50e54
from .verifier import verify_d6e50e54


TASK_ID = "d6e50e54"
generate = generate_d6e50e54
verify = verify_d6e50e54
REFERENCE_TASK_PATH = "data/official/arc2/training/d6e50e54.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d6e50e54",
    "verify",
    "verify_d6e50e54",
]
