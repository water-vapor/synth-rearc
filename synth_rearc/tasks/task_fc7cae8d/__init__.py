from .generator import generate_fc7cae8d
from .verifier import verify_fc7cae8d


TASK_ID = "fc7cae8d"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/fc7cae8d.json"

generate = generate_fc7cae8d
verify = verify_fc7cae8d

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fc7cae8d",
    "verify",
    "verify_fc7cae8d",
]
