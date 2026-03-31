from .generator import generate_53fb4810
from .verifier import verify_53fb4810


TASK_ID = "53fb4810"
generate = generate_53fb4810
verify = verify_53fb4810
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/53fb4810.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_53fb4810",
    "verify",
    "verify_53fb4810",
]
