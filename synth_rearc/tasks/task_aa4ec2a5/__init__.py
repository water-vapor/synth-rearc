from .generator import generate_aa4ec2a5
from .verifier import verify_aa4ec2a5


TASK_ID = "aa4ec2a5"
generate = generate_aa4ec2a5
verify = verify_aa4ec2a5
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/aa4ec2a5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_aa4ec2a5",
    "verify",
    "verify_aa4ec2a5",
]
