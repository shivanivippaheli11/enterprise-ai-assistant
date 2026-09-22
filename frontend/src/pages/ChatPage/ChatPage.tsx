import ChatHeader from "../../components/chat/ChatHeader/ChatHeader";
import MessageList from "../../components/chat/MessageList/MessageList";
import ChatInput from "../../components/chat/ChatInput/ChatInput";

import { useChat } from "../../hooks/useChat";

import "./ChatPage.css";

function ChatPage() {
  const {
    messages,
    input,
    setInput,
    sendMessage,
    isLoading,
    error,
  } = useChat();

  return (
    <main className="chat-page">

      <div className="chat-container">

        <ChatHeader />

        <section className="chat-content">

          <MessageList
            messages={messages}
          />

          {isLoading && (
            <div className="chat-status">
              AI Assistant is thinking...
            </div>
          )}

          {error && (
            <div className="chat-error">
              {error}
            </div>
          )}

        </section>

        <ChatInput
          input={input}
          onInputChange={setInput}
          onSend={sendMessage}
          isLoading={isLoading}
        />

      </div>

    </main>
  );
}

export default ChatPage;