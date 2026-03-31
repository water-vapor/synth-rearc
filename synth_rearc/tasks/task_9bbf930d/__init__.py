from .generator import generate_9bbf930d
from .verifier import verify_9bbf930d


TASK_ID = "9bbf930d"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/9bbf930d.json"

generate = generate_9bbf930d
verify = verify_9bbf930d

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9bbf930d",
    "verify",
    "verify_9bbf930d",
]
