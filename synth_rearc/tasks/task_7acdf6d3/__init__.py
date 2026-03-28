from .generator import generate_7acdf6d3
from .verifier import verify_7acdf6d3


TASK_ID = "7acdf6d3"
generate = generate_7acdf6d3
verify = verify_7acdf6d3
REFERENCE_TASK_PATH = "data/official/arc2/training/7acdf6d3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7acdf6d3",
    "verify",
    "verify_7acdf6d3",
]
