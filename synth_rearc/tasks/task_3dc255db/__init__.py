from .generator import generate_3dc255db
from .verifier import verify_3dc255db


TASK_ID = "3dc255db"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/3dc255db.json"

generate = generate_3dc255db
verify = verify_3dc255db

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3dc255db",
    "verify",
    "verify_3dc255db",
]
