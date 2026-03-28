from .generator import generate_9f669b64
from .verifier import verify_9f669b64


TASK_ID = "9f669b64"
generate = generate_9f669b64
verify = verify_9f669b64
REFERENCE_TASK_PATH = "data/official/arc2/training/9f669b64.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9f669b64",
    "verify",
    "verify_9f669b64",
]
