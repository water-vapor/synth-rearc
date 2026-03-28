from .generator import generate_0becf7df
from .verifier import verify_0becf7df


TASK_ID = "0becf7df"
generate = generate_0becf7df
verify = verify_0becf7df
REFERENCE_TASK_PATH = "data/official/arc2/training/0becf7df.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0becf7df",
    "verify",
    "verify_0becf7df",
]
