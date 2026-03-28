from .generator import generate_08573cc6
from .verifier import verify_08573cc6


TASK_ID = "08573cc6"
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/08573cc6.json"

generate = generate_08573cc6
verify = verify_08573cc6

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_08573cc6",
    "verify",
    "verify_08573cc6",
]
