from .generator import generate_db695cfb
from .verifier import verify_db695cfb


TASK_ID = "db695cfb"
generate = generate_db695cfb
verify = verify_db695cfb
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/db695cfb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_db695cfb",
    "verify",
    "verify_db695cfb",
]
