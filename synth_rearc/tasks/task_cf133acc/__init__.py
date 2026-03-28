from .generator import generate_cf133acc
from .verifier import verify_cf133acc


TASK_ID = "cf133acc"
REFERENCE_TASK_PATH = "data/official/arc2/training/cf133acc.json"

generate = generate_cf133acc
verify = verify_cf133acc

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_cf133acc",
    "verify",
    "verify_cf133acc",
]
