from .generator import generate_e12f9a14
from .verifier import verify_e12f9a14


TASK_ID = "e12f9a14"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/e12f9a14.json"

generate = generate_e12f9a14
verify = verify_e12f9a14

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e12f9a14",
    "verify",
    "verify_e12f9a14",
]
