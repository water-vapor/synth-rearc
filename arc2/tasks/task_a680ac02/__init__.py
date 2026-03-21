from .generator import generate_a680ac02
from .verifier import verify_a680ac02


TASK_ID = "a680ac02"
generate = generate_a680ac02
verify = verify_a680ac02
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/a680ac02.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a680ac02",
    "verify",
    "verify_a680ac02",
]
