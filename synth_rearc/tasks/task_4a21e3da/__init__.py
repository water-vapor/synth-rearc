from .generator import generate_4a21e3da
from .verifier import verify_4a21e3da


TASK_ID = "4a21e3da"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/4a21e3da.json"

generate = generate_4a21e3da
verify = verify_4a21e3da

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4a21e3da",
    "verify",
    "verify_4a21e3da",
]
