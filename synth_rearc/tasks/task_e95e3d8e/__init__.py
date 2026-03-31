from .generator import generate_e95e3d8e
from .verifier import verify_e95e3d8e


TASK_ID = "e95e3d8e"
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/e95e3d8e.json"

generate = generate_e95e3d8e
verify = verify_e95e3d8e

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e95e3d8e",
    "verify",
    "verify_e95e3d8e",
]
