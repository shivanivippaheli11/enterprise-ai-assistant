from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse


def main():
    request = ChatRequest(
        user_id="EMP001",
        session_id="SESSION001",
        message="Summarize the Q2 financial report.",
    )

    response = ChatResponse(
        response_id="RESP001",
        session_id=request.session_id,
        response="The Q2 report has been summarized successfully.",
        status="SUCCESS",
        timestamp="2026-07-30T14:30:00",
    )

    print("===== Chat Request =====")
    print(f"User ID     : {request.user_id}")
    print(f"Session ID  : {request.session_id}")
    print(f"Message     : {request.message}")

    print("\n===== Chat Response =====")
    print(f"Response ID : {response.response_id}")
    print(f"Session ID  : {response.session_id}")
    print(f"Response    : {response.response}")
    print(f"Status      : {response.status}")
    print(f"Timestamp   : {response.timestamp}")


if __name__ == "__main__":
    main()