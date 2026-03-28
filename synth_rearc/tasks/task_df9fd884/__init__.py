from .generator import generate_df9fd884
from .verifier import verify_df9fd884


TASK_ID = "df9fd884"
generate = generate_df9fd884
verify = verify_df9fd884
REFERENCE_TASK_PATH = "data/official/arc2/training/df9fd884.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_df9fd884",
    "verify",
    "verify_df9fd884",
]
