from .generator import generate_a251c730
from .verifier import verify_a251c730


TASK_ID = "a251c730"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/a251c730.json"

generate = generate_a251c730
verify = verify_a251c730

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a251c730",
    "verify",
    "verify_a251c730",
]
