import type { ChatMessage } from "../../../types/chat";

import "./MessageBubble.css";

interface MessageBubbleProps {
  message: ChatMessage;
}

function MessageBubble({
  message,
}: MessageBubbleProps) {
  const isUser = message.role === "user";

  return (
    <article
      className={`message-bubble-wrapper ${
        isUser ? "user-message" : "assistant-message"
      }`}
    >
      <div className="message-bubble">

        <span className="message-sender">
          {isUser ? "You" : "AI Assistant"}
        </span>

        <p className="message-text">
          {message.message}
        </p>

      </div>
    </article>
  );
}

export default MessageBubble;