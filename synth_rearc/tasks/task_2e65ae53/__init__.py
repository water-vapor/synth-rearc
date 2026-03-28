from .generator import generate_2e65ae53
from .verifier import verify_2e65ae53


TASK_ID = "2e65ae53"
generate = generate_2e65ae53
verify = verify_2e65ae53
REFERENCE_TASK_PATH = "data/official/arc2/training/2e65ae53.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2e65ae53",
    "verify",
    "verify_2e65ae53",
]
