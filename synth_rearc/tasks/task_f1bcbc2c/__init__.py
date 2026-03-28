from .generator import generate_f1bcbc2c
from .verifier import verify_f1bcbc2c


TASK_ID = "f1bcbc2c"
generate = generate_f1bcbc2c
verify = verify_f1bcbc2c
REFERENCE_TASK_PATH = "data/official/arc2/training/f1bcbc2c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f1bcbc2c",
    "verify",
    "verify_f1bcbc2c",
]
