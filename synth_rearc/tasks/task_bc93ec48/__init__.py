from .generator import generate_bc93ec48
from .verifier import verify_bc93ec48


TASK_ID = "bc93ec48"
generate = generate_bc93ec48
verify = verify_bc93ec48
REFERENCE_TASK_PATH = "data/official/arc2/training/bc93ec48.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bc93ec48",
    "verify",
    "verify_bc93ec48",
]
