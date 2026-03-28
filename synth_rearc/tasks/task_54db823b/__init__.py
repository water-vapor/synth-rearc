from .generator import generate_54db823b
from .verifier import verify_54db823b


TASK_ID = "54db823b"
generate = generate_54db823b
verify = verify_54db823b
REFERENCE_TASK_PATH = "data/official/arc2/training/54db823b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_54db823b",
    "verify",
    "verify_54db823b",
]
