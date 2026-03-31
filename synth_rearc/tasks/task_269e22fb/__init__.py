from .generator import generate_269e22fb
from .verifier import verify_269e22fb


TASK_ID = "269e22fb"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/269e22fb.json"

generate = generate_269e22fb
verify = verify_269e22fb

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_269e22fb",
    "verify",
    "verify_269e22fb",
]
