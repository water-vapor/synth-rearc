from .generator import generate_a834deea
from .verifier import verify_a834deea


TASK_ID = "a834deea"
generate = generate_a834deea
verify = verify_a834deea
REFERENCE_TASK_PATH = "data/official/arc2/training/a834deea.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a834deea",
    "verify",
    "verify_a834deea",
]
