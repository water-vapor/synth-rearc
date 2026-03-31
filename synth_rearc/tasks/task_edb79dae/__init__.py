from .generator import generate_edb79dae
from .verifier import verify_edb79dae


TASK_ID = "edb79dae"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/edb79dae.json"

generate = generate_edb79dae
verify = verify_edb79dae

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_edb79dae",
    "verify",
    "verify_edb79dae",
]
