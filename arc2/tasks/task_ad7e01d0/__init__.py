from .generator import generate_ad7e01d0
from .verifier import verify_ad7e01d0


TASK_ID = "ad7e01d0"
generate = generate_ad7e01d0
verify = verify_ad7e01d0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ad7e01d0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ad7e01d0",
    "verify",
    "verify_ad7e01d0",
]
