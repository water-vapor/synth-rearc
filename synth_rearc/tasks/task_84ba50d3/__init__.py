from .generator import generate_84ba50d3
from .verifier import verify_84ba50d3


TASK_ID = "84ba50d3"
REFERENCE_TASK_PATH = "data/official/arc2/training/84ba50d3.json"

generate = generate_84ba50d3
verify = verify_84ba50d3

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_84ba50d3",
    "verify",
    "verify_84ba50d3",
]
