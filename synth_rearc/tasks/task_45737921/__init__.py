from .generator import generate_45737921
from .verifier import verify_45737921


TASK_ID = "45737921"
generate = generate_45737921
verify = verify_45737921
REFERENCE_TASK_PATH = "data/official/arc2/training/45737921.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_45737921",
    "verify",
    "verify_45737921",
]
