from .generator import generate_423a55dc
from .verifier import verify_423a55dc


TASK_ID = "423a55dc"
generate = generate_423a55dc
verify = verify_423a55dc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/423a55dc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_423a55dc",
    "verify",
    "verify_423a55dc",
]
