from .generator import generate_dfadab01
from .verifier import verify_dfadab01


TASK_ID = "dfadab01"
generate = generate_dfadab01
verify = verify_dfadab01
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/dfadab01.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_dfadab01",
    "verify",
    "verify_dfadab01",
]
