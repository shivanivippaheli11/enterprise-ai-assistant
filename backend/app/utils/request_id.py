import uuid


def generate_request_id() -> str:
    """
    Generates a unique request ID.
    """

    return f"REQ-{uuid.uuid4().hex[:8].upper()}"