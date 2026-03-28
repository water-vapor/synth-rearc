from .generator import generate_e45ef808
from .verifier import verify_e45ef808


TASK_ID = "e45ef808"
generate = generate_e45ef808
verify = verify_e45ef808
REFERENCE_TASK_PATH = "data/official/arc2/training/e45ef808.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e45ef808",
    "verify",
    "verify_e45ef808",
]
