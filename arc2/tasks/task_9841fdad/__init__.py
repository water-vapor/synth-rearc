from .generator import generate_9841fdad
from .verifier import verify_9841fdad


TASK_ID = "9841fdad"
generate = generate_9841fdad
verify = verify_9841fdad
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9841fdad.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9841fdad",
    "verify",
    "verify_9841fdad",
]
