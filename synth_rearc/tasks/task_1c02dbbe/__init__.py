from .generator import generate_1c02dbbe
from .verifier import verify_1c02dbbe


TASK_ID = "1c02dbbe"
generate = generate_1c02dbbe
verify = verify_1c02dbbe
REFERENCE_TASK_PATH = "data/official/arc2/training/1c02dbbe.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1c02dbbe",
    "verify",
    "verify_1c02dbbe",
]
