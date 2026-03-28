from .generator import generate_aab50785
from .verifier import verify_aab50785


TASK_ID = "aab50785"
generate = generate_aab50785
verify = verify_aab50785
REFERENCE_TASK_PATH = "data/official/arc2/training/aab50785.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_aab50785",
    "verify",
    "verify_aab50785",
]
