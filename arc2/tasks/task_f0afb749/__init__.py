from .generator import generate_f0afb749
from .verifier import verify_f0afb749


TASK_ID = "f0afb749"
generate = generate_f0afb749
verify = verify_f0afb749
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f0afb749.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f0afb749",
    "verify",
    "verify_f0afb749",
]
