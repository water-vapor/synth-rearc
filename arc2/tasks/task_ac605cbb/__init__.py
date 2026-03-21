from .generator import generate_ac605cbb
from .verifier import verify_ac605cbb


TASK_ID = "ac605cbb"
generate = generate_ac605cbb
verify = verify_ac605cbb
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ac605cbb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ac605cbb",
    "verify",
    "verify_ac605cbb",
]
