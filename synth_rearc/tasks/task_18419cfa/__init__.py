from .generator import generate_18419cfa
from .verifier import verify_18419cfa


TASK_ID = "18419cfa"
generate = generate_18419cfa
verify = verify_18419cfa
REFERENCE_TASK_PATH = "data/official/arc2/training/18419cfa.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_18419cfa",
    "verify",
    "verify_18419cfa",
]
