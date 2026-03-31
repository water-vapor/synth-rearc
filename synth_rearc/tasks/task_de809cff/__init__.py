from .generator import generate_de809cff
from .verifier import verify_de809cff


TASK_ID = "de809cff"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/de809cff.json"

generate = generate_de809cff
verify = verify_de809cff

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_de809cff",
    "verify",
    "verify_de809cff",
]
