from .generator import generate_bf45cf4b
from .verifier import verify_bf45cf4b


TASK_ID = "bf45cf4b"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/bf45cf4b.json"

generate = generate_bf45cf4b
verify = verify_bf45cf4b

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bf45cf4b",
    "verify",
    "verify_bf45cf4b",
]
