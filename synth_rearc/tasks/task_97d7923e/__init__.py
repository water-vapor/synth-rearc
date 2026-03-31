from .generator import generate_97d7923e
from .verifier import verify_97d7923e


TASK_ID = "97d7923e"
generate = generate_97d7923e
verify = verify_97d7923e
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/97d7923e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_97d7923e",
    "verify",
    "verify_97d7923e",
]
