from .generator import generate_cad67732
from .verifier import verify_cad67732


TASK_ID = "cad67732"
generate = generate_cad67732
verify = verify_cad67732
REFERENCE_TASK_PATH = "data/official/arc2/training/cad67732.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_cad67732",
    "verify",
    "verify_cad67732",
]
