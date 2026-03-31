from .generator import generate_136b0064
from .verifier import verify_136b0064


TASK_ID = "136b0064"
generate = generate_136b0064
verify = verify_136b0064
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/136b0064.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_136b0064",
    "verify",
    "verify_136b0064",
]
