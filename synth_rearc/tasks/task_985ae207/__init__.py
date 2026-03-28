from .generator import generate_985ae207
from .verifier import verify_985ae207


TASK_ID = "985ae207"
generate = generate_985ae207
verify = verify_985ae207
REFERENCE_TASK_PATH = "data/official/arc2/training/985ae207.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_985ae207",
    "verify",
    "verify_985ae207",
]
