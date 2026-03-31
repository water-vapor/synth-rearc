from .generator import generate_80a900e0
from .verifier import verify_80a900e0


TASK_ID = "80a900e0"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/80a900e0.json"

generate = generate_80a900e0
verify = verify_80a900e0

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_80a900e0",
    "verify",
    "verify_80a900e0",
]
