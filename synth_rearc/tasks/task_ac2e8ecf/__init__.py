from .generator import generate_ac2e8ecf
from .verifier import verify_ac2e8ecf


TASK_ID = "ac2e8ecf"
generate = generate_ac2e8ecf
verify = verify_ac2e8ecf
REFERENCE_TASK_PATH = "data/official/arc2/training/ac2e8ecf.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ac2e8ecf",
    "verify",
    "verify_ac2e8ecf",
]
