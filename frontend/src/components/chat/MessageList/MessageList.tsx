import { useEffect, useRef } from "react";

import type { ChatMessage } from "../../../types/chat";

import MessageBubble from "../MessageBubble/MessageBubble";

import "./MessageList.css";

interface MessageListProps {
  messages: ChatMessage[];
}

function MessageList({
  messages,
}: MessageListProps) {

  const bottomRef = useRef<HTMLDivElement | null>(
    null
  );

  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });

  }, [messages]);

  return (
    <section className="message-list">

      {messages.length === 0 ? (
        <div className="empty-chat">

          <div className="empty-chat-icon">
            AI
          </div>

          <h2>
            How can I help you?
          </h2>

          <p>
            Ask a question and I'll do my best to assist you.
          </p>

        </div>
      ) : (
        messages.map((message) => (
          <MessageBubble
            key={message.id}
            message={message}
          />
        ))
      )}

      <div ref={bottomRef} />

    </section>
  );
}

export default MessageList;