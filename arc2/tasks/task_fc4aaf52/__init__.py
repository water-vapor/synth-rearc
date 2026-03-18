from .generator import generate_fc4aaf52
from .verifier import verify_fc4aaf52


TASK_ID = "fc4aaf52"
generate = generate_fc4aaf52
verify = verify_fc4aaf52
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/fc4aaf52.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fc4aaf52",
    "verify",
    "verify_fc4aaf52",
]
