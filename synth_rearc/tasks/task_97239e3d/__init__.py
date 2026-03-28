from .generator import generate_97239e3d
from .verifier import verify_97239e3d


TASK_ID = "97239e3d"
generate = generate_97239e3d
verify = verify_97239e3d
REFERENCE_TASK_PATH = "data/official/arc2/training/97239e3d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_97239e3d",
    "verify",
    "verify_97239e3d",
]
