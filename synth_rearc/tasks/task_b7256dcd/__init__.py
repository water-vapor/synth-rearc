from .generator import generate_b7256dcd
from .verifier import verify_b7256dcd


TASK_ID = "b7256dcd"
generate = generate_b7256dcd
verify = verify_b7256dcd
REFERENCE_TASK_PATH = "data/official/arc2/training/b7256dcd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b7256dcd",
    "verify",
    "verify_b7256dcd",
]
