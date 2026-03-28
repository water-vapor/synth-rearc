from .generator import generate_3a301edc
from .verifier import verify_3a301edc


TASK_ID = "3a301edc"
generate = generate_3a301edc
verify = verify_3a301edc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/3a301edc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3a301edc",
    "verify",
    "verify_3a301edc",
]
