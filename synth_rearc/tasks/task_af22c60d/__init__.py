from .generator import generate_af22c60d
from .verifier import verify_af22c60d


TASK_ID = "af22c60d"
generate = generate_af22c60d
verify = verify_af22c60d
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/af22c60d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_af22c60d",
    "verify",
    "verify_af22c60d",
]
