from .generator import generate_3d588dc9
from .verifier import verify_3d588dc9


TASK_ID = "3d588dc9"
generate = generate_3d588dc9
verify = verify_3d588dc9
REFERENCE_TASK_PATH = "data/official/arc2/training/3d588dc9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3d588dc9",
    "verify",
    "verify_3d588dc9",
]
