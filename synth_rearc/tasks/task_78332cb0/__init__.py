from .generator import generate_78332cb0
from .verifier import verify_78332cb0


TASK_ID = "78332cb0"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/78332cb0.json"
generate = generate_78332cb0
verify = verify_78332cb0


__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_78332cb0",
    "verify",
    "verify_78332cb0",
]
