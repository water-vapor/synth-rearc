from .generator import generate_98c475bf
from .verifier import verify_98c475bf


TASK_ID = "98c475bf"
generate = generate_98c475bf
verify = verify_98c475bf
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/98c475bf.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_98c475bf",
    "verify",
    "verify_98c475bf",
]
