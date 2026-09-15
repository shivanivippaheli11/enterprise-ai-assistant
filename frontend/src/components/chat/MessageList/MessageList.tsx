import type { ChatMessage } from "../../../types/chat";

import MessageBubble from "../MessageBubble/MessageBubble";

import "./MessageList.css";


interface MessageListProps {
  messages: ChatMessage[];
}


function MessageList({
  messages,
}: MessageListProps) {

  return (
    <section className="message-list">

      {messages.map((message, index) => (
        <MessageBubble
          key={index}
          message={message}
        />
      ))}

    </section>
  );
}


export default MessageList;