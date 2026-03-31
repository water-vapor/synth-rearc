from .generator import generate_38007db0
from .verifier import verify_38007db0


TASK_ID = "38007db0"
generate = generate_38007db0
verify = verify_38007db0
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/38007db0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_38007db0",
    "verify",
    "verify_38007db0",
]
