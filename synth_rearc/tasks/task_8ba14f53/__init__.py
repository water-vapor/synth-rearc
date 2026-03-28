from .generator import generate_8ba14f53
from .verifier import verify_8ba14f53


TASK_ID = "8ba14f53"
generate = generate_8ba14f53
verify = verify_8ba14f53
REFERENCE_TASK_PATH = "data/official/arc2/training/8ba14f53.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8ba14f53",
    "verify",
    "verify_8ba14f53",
]
