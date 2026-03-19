from .generator import generate_de493100
from .verifier import verify_de493100


TASK_ID = "de493100"
generate = generate_de493100
verify = verify_de493100
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/de493100.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_de493100",
    "verify",
    "verify_de493100",
]
