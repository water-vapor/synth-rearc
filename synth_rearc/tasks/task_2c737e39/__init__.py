from .generator import generate_2c737e39
from .verifier import verify_2c737e39


TASK_ID = "2c737e39"
generate = generate_2c737e39
verify = verify_2c737e39
REFERENCE_TASK_PATH = "data/official/arc2/training/2c737e39.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2c737e39",
    "verify",
    "verify_2c737e39",
]
