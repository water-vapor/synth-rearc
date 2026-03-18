from .generator import generate_ff2825db
from .verifier import verify_ff2825db


TASK_ID = "ff2825db"
generate = generate_ff2825db
verify = verify_ff2825db
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ff2825db.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ff2825db",
    "verify",
    "verify_ff2825db",
]
