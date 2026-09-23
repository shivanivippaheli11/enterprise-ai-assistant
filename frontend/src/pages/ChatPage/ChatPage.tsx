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
    retryLastMessage,
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
            <div className="typing-indicator-wrapper">

              <div className="typing-indicator">

                <span className="typing-label">
                  AI Assistant
                </span>

                <div className="typing-dots">
                  <span />
                  <span />
                  <span />
                </div>

              </div>

            </div>
          )}

          {error && (
            <div className="chat-error">

              <span>
                {error}
              </span>

              <button
                onClick={retryLastMessage}
                disabled={isLoading}
              >
                Retry
              </button>

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