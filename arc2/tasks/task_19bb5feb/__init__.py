from .generator import generate_19bb5feb
from .verifier import verify_19bb5feb


TASK_ID = "19bb5feb"
generate = generate_19bb5feb
verify = verify_19bb5feb
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/19bb5feb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_19bb5feb",
    "verify",
    "verify_19bb5feb",
]
