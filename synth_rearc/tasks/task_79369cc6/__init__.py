from .generator import generate_79369cc6
from .verifier import verify_79369cc6


TASK_ID = "79369cc6"
generate = generate_79369cc6
verify = verify_79369cc6
REFERENCE_TASK_PATH = "data/official/arc2/training/79369cc6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_79369cc6",
    "verify",
    "verify_79369cc6",
]
