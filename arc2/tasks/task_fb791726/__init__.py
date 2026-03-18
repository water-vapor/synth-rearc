from .generator import generate_fb791726
from .verifier import verify_fb791726


TASK_ID = "fb791726"
generate = generate_fb791726
verify = verify_fb791726
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/fb791726.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fb791726",
    "verify",
    "verify_fb791726",
]
