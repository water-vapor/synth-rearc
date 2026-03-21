from .generator import generate_a934301b
from .verifier import verify_a934301b


TASK_ID = "a934301b"
generate = generate_a934301b
verify = verify_a934301b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/a934301b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a934301b",
    "verify",
    "verify_a934301b",
]
