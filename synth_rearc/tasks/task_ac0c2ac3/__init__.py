from .generator import generate_ac0c2ac3
from .verifier import verify_ac0c2ac3


TASK_ID = "ac0c2ac3"
generate = generate_ac0c2ac3
verify = verify_ac0c2ac3
REFERENCE_TASK_PATH = "data/official/arc2/training/ac0c2ac3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ac0c2ac3",
    "verify",
    "verify_ac0c2ac3",
]
