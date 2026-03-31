from .generator import generate_89565ca0
from .verifier import verify_89565ca0


TASK_ID = "89565ca0"
generate = generate_89565ca0
verify = verify_89565ca0
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/89565ca0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_89565ca0",
    "verify",
    "verify_89565ca0",
]
