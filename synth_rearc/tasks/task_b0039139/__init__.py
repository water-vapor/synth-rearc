from .generator import generate_b0039139
from .verifier import verify_b0039139


TASK_ID = "b0039139"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/b0039139.json"

generate = generate_b0039139
verify = verify_b0039139

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b0039139",
    "verify",
    "verify_b0039139",
]
