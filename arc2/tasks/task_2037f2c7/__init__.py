from .generator import generate_2037f2c7
from .verifier import verify_2037f2c7


TASK_ID = "2037f2c7"
generate = generate_2037f2c7
verify = verify_2037f2c7
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/2037f2c7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2037f2c7",
    "verify",
    "verify_2037f2c7",
]
