from .generator import generate_e0fb7511
from .verifier import verify_e0fb7511


TASK_ID = "e0fb7511"
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e0fb7511.json"

generate = generate_e0fb7511
verify = verify_e0fb7511


__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "verify",
    "generate_e0fb7511",
    "verify_e0fb7511",
]
