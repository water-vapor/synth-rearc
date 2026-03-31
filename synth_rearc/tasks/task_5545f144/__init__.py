from .generator import generate_5545f144
from .verifier import verify_5545f144


TASK_ID = "5545f144"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/5545f144.json"

generate = generate_5545f144
verify = verify_5545f144

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5545f144",
    "verify",
    "verify_5545f144",
]
