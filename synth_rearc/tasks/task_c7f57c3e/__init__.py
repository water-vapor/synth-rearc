from .generator import generate_c7f57c3e
from .verifier import verify_c7f57c3e


TASK_ID = "c7f57c3e"
generate = generate_c7f57c3e
verify = verify_c7f57c3e
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/c7f57c3e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c7f57c3e",
    "verify",
    "verify_c7f57c3e",
]
