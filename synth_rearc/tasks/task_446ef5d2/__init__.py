from .generator import generate_446ef5d2
from .verifier import verify_446ef5d2


TASK_ID = "446ef5d2"
generate = generate_446ef5d2
verify = verify_446ef5d2
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/446ef5d2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_446ef5d2",
    "verify",
    "verify_446ef5d2",
]
