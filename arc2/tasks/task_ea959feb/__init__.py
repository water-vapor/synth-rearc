from .generator import generate_ea959feb
from .verifier import verify_ea959feb


TASK_ID = "ea959feb"
generate = generate_ea959feb
verify = verify_ea959feb
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ea959feb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ea959feb",
    "verify",
    "verify_ea959feb",
]
