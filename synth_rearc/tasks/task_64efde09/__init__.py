from .generator import generate_64efde09
from .verifier import verify_64efde09


TASK_ID = "64efde09"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/64efde09.json"

generate = generate_64efde09
verify = verify_64efde09

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_64efde09",
    "verify",
    "verify_64efde09",
]
