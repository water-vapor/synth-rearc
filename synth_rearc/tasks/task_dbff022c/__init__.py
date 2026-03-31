from .generator import generate_dbff022c
from .verifier import verify_dbff022c


TASK_ID = "dbff022c"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/dbff022c.json"

generate = generate_dbff022c
verify = verify_dbff022c

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_dbff022c",
    "verify",
    "verify_dbff022c",
]
