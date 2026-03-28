from .generator import generate_df978a02
from .verifier import verify_df978a02


TASK_ID = "df978a02"
generate = generate_df978a02
verify = verify_df978a02
REFERENCE_TASK_PATH = "data/official/arc2/training/df978a02.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_df978a02",
    "verify",
    "verify_df978a02",
]
