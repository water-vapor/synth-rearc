from .generator import generate_20fb2937
from .verifier import verify_20fb2937


TASK_ID = "20fb2937"
generate = generate_20fb2937
verify = verify_20fb2937
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/20fb2937.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_20fb2937",
    "verify",
    "verify_20fb2937",
]
