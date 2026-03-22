from .generator import generate_6ad5bdfd
from .verifier import verify_6ad5bdfd


TASK_ID = "6ad5bdfd"
generate = generate_6ad5bdfd
verify = verify_6ad5bdfd
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/6ad5bdfd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6ad5bdfd",
    "verify",
    "verify_6ad5bdfd",
]
