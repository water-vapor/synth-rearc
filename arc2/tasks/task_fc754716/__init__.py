from .generator import generate_fc754716
from .verifier import verify_fc754716


TASK_ID = "fc754716"
generate = generate_fc754716
verify = verify_fc754716
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/fc754716.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fc754716",
    "verify",
    "verify_fc754716",
]
