from .generator import generate_0bb8deee
from .verifier import verify_0bb8deee


TASK_ID = "0bb8deee"
generate = generate_0bb8deee
verify = verify_0bb8deee
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/0bb8deee.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0bb8deee",
    "verify",
    "verify_0bb8deee",
]
