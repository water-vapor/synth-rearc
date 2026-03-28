from .generator import generate_67c52801
from .verifier import verify_67c52801


TASK_ID = "67c52801"
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/67c52801.json"

generate = generate_67c52801
verify = verify_67c52801

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_67c52801",
    "verify",
    "verify_67c52801",
]
