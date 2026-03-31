from .generator import generate_6ffbe589
from .verifier import verify_6ffbe589


TASK_ID = "6ffbe589"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/6ffbe589.json"

generate = generate_6ffbe589
verify = verify_6ffbe589

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6ffbe589",
    "verify",
    "verify_6ffbe589",
]
