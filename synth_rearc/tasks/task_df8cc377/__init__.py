from .generator import generate_df8cc377
from .verifier import verify_df8cc377


TASK_ID = "df8cc377"
generate = generate_df8cc377
verify = verify_df8cc377
REFERENCE_TASK_PATH = "data/official/arc2/training/df8cc377.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_df8cc377",
    "verify",
    "verify_df8cc377",
]
