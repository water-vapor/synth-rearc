from .generator import generate_604001fa
from .verifier import verify_604001fa


TASK_ID = "604001fa"
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/604001fa.json"

generate = generate_604001fa
verify = verify_604001fa

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_604001fa",
    "verify",
    "verify_604001fa",
]
