from .generator import generate_73182012
from .verifier import verify_73182012


TASK_ID = "73182012"
generate = generate_73182012
verify = verify_73182012
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/73182012.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_73182012",
    "verify",
    "verify_73182012",
]
