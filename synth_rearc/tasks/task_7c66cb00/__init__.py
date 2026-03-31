from .generator import generate_7c66cb00
from .verifier import verify_7c66cb00


TASK_ID = "7c66cb00"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/7c66cb00.json"

generate = generate_7c66cb00
verify = verify_7c66cb00

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7c66cb00",
    "verify",
    "verify_7c66cb00",
]
