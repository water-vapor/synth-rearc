from .generator import generate_88e364bc
from .verifier import verify_88e364bc


TASK_ID = "88e364bc"
generate = generate_88e364bc
verify = verify_88e364bc
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/88e364bc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_88e364bc",
    "verify",
    "verify_88e364bc",
]
