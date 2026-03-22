from .generator import generate_9344f635
from .verifier import verify_9344f635


TASK_ID = "9344f635"
generate = generate_9344f635
verify = verify_9344f635
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9344f635.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9344f635",
    "verify",
    "verify_9344f635",
]
