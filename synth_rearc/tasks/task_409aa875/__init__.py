from .generator import generate_409aa875
from .verifier import verify_409aa875


TASK_ID = "409aa875"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/409aa875.json"

generate = generate_409aa875
verify = verify_409aa875

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_409aa875",
    "verify",
    "verify_409aa875",
]
