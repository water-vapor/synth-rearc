from .generator import generate_db0c5428
from .verifier import verify_db0c5428


TASK_ID = "db0c5428"
generate = generate_db0c5428
verify = verify_db0c5428
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/db0c5428.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_db0c5428",
    "verify",
    "verify_db0c5428",
]
