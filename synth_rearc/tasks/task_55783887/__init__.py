from .generator import generate_55783887
from .verifier import verify_55783887


TASK_ID = "55783887"
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/55783887.json"

generate = generate_55783887
verify = verify_55783887

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_55783887",
    "verify",
    "verify_55783887",
]
