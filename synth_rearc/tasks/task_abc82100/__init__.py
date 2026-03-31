from .generator import generate_abc82100
from .verifier import verify_abc82100


TASK_ID = "abc82100"
generate = generate_abc82100
verify = verify_abc82100
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/abc82100.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_abc82100",
    "verify",
    "verify_abc82100",
]
