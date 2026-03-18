from .generator import generate_fafd9572
from .verifier import verify_fafd9572


TASK_ID = "fafd9572"
generate = generate_fafd9572
verify = verify_fafd9572
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/fafd9572.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fafd9572",
    "verify",
    "verify_fafd9572",
]
