from .generator import generate_ae58858e
from .verifier import verify_ae58858e


TASK_ID = "ae58858e"
generate = generate_ae58858e
verify = verify_ae58858e
REFERENCE_TASK_PATH = "data/official/arc2/training/ae58858e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ae58858e",
    "verify",
    "verify_ae58858e",
]
