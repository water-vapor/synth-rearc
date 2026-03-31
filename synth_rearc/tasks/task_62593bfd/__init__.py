from .generator import generate_62593bfd
from .verifier import verify_62593bfd


TASK_ID = "62593bfd"
generate = generate_62593bfd
verify = verify_62593bfd
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/62593bfd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_62593bfd",
    "verify",
    "verify_62593bfd",
]
