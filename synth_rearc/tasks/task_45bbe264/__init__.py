from .generator import generate_45bbe264
from .verifier import verify_45bbe264


TASK_ID = "45bbe264"
generate = generate_45bbe264
verify = verify_45bbe264
REFERENCE_TASK_PATH = "data/official/arc2/training/45bbe264.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_45bbe264",
    "verify",
    "verify_45bbe264",
]
