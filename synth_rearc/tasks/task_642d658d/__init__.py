from .generator import generate_642d658d
from .verifier import verify_642d658d


TASK_ID = "642d658d"
generate = generate_642d658d
verify = verify_642d658d
REFERENCE_TASK_PATH = "data/official/arc2/training/642d658d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_642d658d",
    "verify",
    "verify_642d658d",
]
