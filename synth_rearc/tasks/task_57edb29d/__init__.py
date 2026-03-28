from .generator import generate_57edb29d
from .verifier import verify_57edb29d


TASK_ID = "57edb29d"
REFERENCE_TASK_PATH = "data/official/arc2/training/57edb29d.json"

generate = generate_57edb29d
verify = verify_57edb29d

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_57edb29d",
    "verify",
    "verify_57edb29d",
]
