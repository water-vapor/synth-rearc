from .generator import generate_a47bf94d
from .verifier import verify_a47bf94d


TASK_ID = "a47bf94d"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/a47bf94d.json"

generate = generate_a47bf94d
verify = verify_a47bf94d

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a47bf94d",
    "verify",
    "verify_a47bf94d",
]
