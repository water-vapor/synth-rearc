from .generator import generate_9968a131
from .verifier import verify_9968a131


TASK_ID = "9968a131"
REFERENCE_TASK_PATH = "data/official/arc2/training/9968a131.json"

generate = generate_9968a131
verify = verify_9968a131

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9968a131",
    "verify",
    "verify_9968a131",
]
