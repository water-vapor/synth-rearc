from .generator import generate_ad3b40cf
from .verifier import verify_ad3b40cf


TASK_ID = "ad3b40cf"
generate = generate_ad3b40cf
verify = verify_ad3b40cf
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ad3b40cf.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ad3b40cf",
    "verify",
    "verify_ad3b40cf",
]
