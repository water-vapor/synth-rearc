from .generator import generate_b6f77b65
from .verifier import verify_b6f77b65


TASK_ID = "b6f77b65"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/b6f77b65.json"

generate = generate_b6f77b65
verify = verify_b6f77b65

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b6f77b65",
    "verify",
    "verify_b6f77b65",
]
