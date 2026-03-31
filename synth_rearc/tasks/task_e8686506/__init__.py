from .generator import generate_e8686506
from .verifier import verify_e8686506


TASK_ID = "e8686506"
generate = generate_e8686506
verify = verify_e8686506
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/e8686506.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e8686506",
    "verify",
    "verify_e8686506",
]
