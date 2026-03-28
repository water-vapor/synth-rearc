from .generator import generate_fc10701f
from .verifier import verify_fc10701f


TASK_ID = "fc10701f"
generate = generate_fc10701f
verify = verify_fc10701f
REFERENCE_TASK_PATH = "data/official/arc2/training/fc10701f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fc10701f",
    "verify",
    "verify_fc10701f",
]
