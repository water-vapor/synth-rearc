from .generator import generate_2c181942
from .verifier import verify_2c181942


TASK_ID = "2c181942"
generate = generate_2c181942
verify = verify_2c181942
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/2c181942.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2c181942",
    "verify",
    "verify_2c181942",
]
