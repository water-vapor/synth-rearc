from .generator import generate_79cce52d
from .verifier import verify_79cce52d


TASK_ID = "79cce52d"
generate = generate_79cce52d
verify = verify_79cce52d
REFERENCE_TASK_PATH = "data/official/arc2/training/79cce52d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_79cce52d",
    "verify",
    "verify_79cce52d",
]
