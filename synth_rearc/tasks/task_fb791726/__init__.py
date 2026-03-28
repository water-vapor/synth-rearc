from .generator import generate_fb791726
from .verifier import verify_fb791726


TASK_ID = "fb791726"
generate = generate_fb791726
verify = verify_fb791726
REFERENCE_TASK_PATH = "data/official/arc2/training/fb791726.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fb791726",
    "verify",
    "verify_fb791726",
]
