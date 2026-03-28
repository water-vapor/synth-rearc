from .generator import generate_2f767503
from .verifier import verify_2f767503


TASK_ID = "2f767503"
generate = generate_2f767503
verify = verify_2f767503
REFERENCE_TASK_PATH = "data/official/arc2/training/2f767503.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2f767503",
    "verify",
    "verify_2f767503",
]
