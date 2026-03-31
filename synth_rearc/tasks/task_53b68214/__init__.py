from .generator import generate_53b68214
from .verifier import verify_53b68214


TASK_ID = "53b68214"
generate = generate_53b68214
verify = verify_53b68214
REFERENCE_TASK_PATH = "data/official/arc1/training/53b68214.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_53b68214",
    "verify",
    "verify_53b68214",
]
