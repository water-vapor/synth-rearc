from .generator import generate_f560132c
from .verifier import verify_f560132c


TASK_ID = "f560132c"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/f560132c.json"

generate = generate_f560132c
verify = verify_f560132c

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f560132c",
    "verify",
    "verify_f560132c",
]
