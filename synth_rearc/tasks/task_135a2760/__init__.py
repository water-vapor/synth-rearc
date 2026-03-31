from .generator import generate_135a2760
from .verifier import verify_135a2760


TASK_ID = "135a2760"
generate = generate_135a2760
verify = verify_135a2760
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/135a2760.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_135a2760",
    "verify",
    "verify_135a2760",
]
