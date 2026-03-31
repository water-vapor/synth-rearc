from .generator import generate_65b59efc
from .verifier import verify_65b59efc


TASK_ID = "65b59efc"
generate = generate_65b59efc
verify = verify_65b59efc
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/65b59efc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_65b59efc",
    "verify",
    "verify_65b59efc",
]
