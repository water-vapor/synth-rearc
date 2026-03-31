from .generator import generate_9aaea919
from .verifier import verify_9aaea919


TASK_ID = "9aaea919"
generate = generate_9aaea919
verify = verify_9aaea919
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/9aaea919.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9aaea919",
    "verify",
    "verify_9aaea919",
]
