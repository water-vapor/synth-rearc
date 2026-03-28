from .generator import generate_95a58926
from .verifier import verify_95a58926


TASK_ID = "95a58926"
generate = generate_95a58926
verify = verify_95a58926
REFERENCE_TASK_PATH = "data/official/arc2/training/95a58926.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_95a58926",
    "verify",
    "verify_95a58926",
]
