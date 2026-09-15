import type { ChatMessage } from "../../../types/chat";

import "./MessageBubble.css";


interface MessageBubbleProps {
  message: ChatMessage;
}


function MessageBubble({
  message,
}: MessageBubbleProps) {

  return (
    <article
      className={`message-bubble ${message.role}`}
    >

      <strong>
        {message.role === "user"
          ? "You"
          : "AI Assistant"}
      </strong>

      <p>
        {message.message}
      </p>

    </article>
  );
}


export default MessageBubble;