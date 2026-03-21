from .generator import generate_af726779
from .verifier import verify_af726779


TASK_ID = "af726779"
generate = generate_af726779
verify = verify_af726779
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/af726779.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_af726779",
    "verify",
    "verify_af726779",
]
