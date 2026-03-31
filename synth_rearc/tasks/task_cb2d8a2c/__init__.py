from .generator import generate_cb2d8a2c
from .verifier import verify_cb2d8a2c


TASK_ID = "cb2d8a2c"
generate = generate_cb2d8a2c
verify = verify_cb2d8a2c
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/cb2d8a2c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_cb2d8a2c",
    "verify",
    "verify_cb2d8a2c",
]
