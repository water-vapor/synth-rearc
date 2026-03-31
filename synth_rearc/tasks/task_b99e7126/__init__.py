from .generator import generate_b99e7126
from .verifier import verify_b99e7126


TASK_ID = "b99e7126"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/b99e7126.json"

generate = generate_b99e7126
verify = verify_b99e7126

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b99e7126",
    "verify",
    "verify_b99e7126",
]
