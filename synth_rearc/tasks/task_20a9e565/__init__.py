from .generator import generate_20a9e565
from .verifier import verify_20a9e565


TASK_ID = "20a9e565"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/20a9e565.json"

generate = generate_20a9e565
verify = verify_20a9e565

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_20a9e565",
    "verify",
    "verify_20a9e565",
]
