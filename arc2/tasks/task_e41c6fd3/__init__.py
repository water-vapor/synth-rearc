from .generator import generate_e41c6fd3
from .verifier import verify_e41c6fd3


TASK_ID = "e41c6fd3"
generate = generate_e41c6fd3
verify = verify_e41c6fd3
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e41c6fd3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e41c6fd3",
    "verify",
    "verify_e41c6fd3",
]
