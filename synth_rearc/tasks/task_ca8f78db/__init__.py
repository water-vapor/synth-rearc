from .generator import generate_ca8f78db
from .verifier import verify_ca8f78db


TASK_ID = "ca8f78db"
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/ca8f78db.json"

generate = generate_ca8f78db
verify = verify_ca8f78db

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ca8f78db",
    "verify",
    "verify_ca8f78db",
]
