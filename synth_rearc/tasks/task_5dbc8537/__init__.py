from .generator import generate_5dbc8537
from .verifier import verify_5dbc8537


TASK_ID = "5dbc8537"
generate = generate_5dbc8537
verify = verify_5dbc8537
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/5dbc8537.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5dbc8537",
    "verify",
    "verify_5dbc8537",
]
