from .generator import generate_84db8fc4
from .verifier import verify_84db8fc4


TASK_ID = "84db8fc4"
generate = generate_84db8fc4
verify = verify_84db8fc4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/84db8fc4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_84db8fc4",
    "verify",
    "verify_84db8fc4",
]
