from .generator import generate_652646ff
from .verifier import verify_652646ff


TASK_ID = "652646ff"
generate = generate_652646ff
verify = verify_652646ff
REFERENCE_TASK_PATH = "data/official/arc2/training/652646ff.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_652646ff",
    "verify",
    "verify_652646ff",
]
