from .generator import generate_184a9768
from .verifier import verify_184a9768


TASK_ID = "184a9768"
generate = generate_184a9768
verify = verify_184a9768
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/184a9768.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_184a9768",
    "verify",
    "verify_184a9768",
]
