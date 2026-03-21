from .generator import generate_a57f2f04
from .verifier import verify_a57f2f04


TASK_ID = "a57f2f04"
generate = generate_a57f2f04
verify = verify_a57f2f04
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/a57f2f04.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a57f2f04",
    "verify",
    "verify_a57f2f04",
]
