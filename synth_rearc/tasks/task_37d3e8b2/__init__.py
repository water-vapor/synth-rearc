from .generator import generate_37d3e8b2
from .verifier import verify_37d3e8b2


TASK_ID = "37d3e8b2"
generate = generate_37d3e8b2
verify = verify_37d3e8b2
REFERENCE_TASK_PATH = "data/official/arc2/training/37d3e8b2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_37d3e8b2",
    "verify",
    "verify_37d3e8b2",
]
