from .generator import generate_83eb0a57
from .verifier import verify_83eb0a57


TASK_ID = "83eb0a57"
generate = generate_83eb0a57
verify = verify_83eb0a57
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/83eb0a57.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_83eb0a57",
    "verify",
    "verify_83eb0a57",
]
