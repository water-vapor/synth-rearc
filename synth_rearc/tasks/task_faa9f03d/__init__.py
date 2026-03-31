from .generator import generate_faa9f03d
from .verifier import verify_faa9f03d


TASK_ID = "faa9f03d"
generate = generate_faa9f03d
verify = verify_faa9f03d
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/faa9f03d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_faa9f03d",
    "verify",
    "verify_faa9f03d",
]
