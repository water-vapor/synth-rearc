from .generator import generate_973e499e
from .verifier import verify_973e499e


TASK_ID = "973e499e"
generate = generate_973e499e
verify = verify_973e499e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/973e499e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_973e499e",
    "verify",
    "verify_973e499e",
]
