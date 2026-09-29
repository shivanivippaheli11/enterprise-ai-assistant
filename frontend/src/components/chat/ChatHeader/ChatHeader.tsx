import "./ChatHeader.css";

interface ChatHeaderProps {
  onNewChat: () => void;
}

function ChatHeader({
  onNewChat,
}: ChatHeaderProps) {

  return (
    <header className="chat-header">

      <div className="chat-header-content">

        <div>
          <h1>
            Enterprise AI Assistant
          </h1>

          <p>
            Ask questions and get assistance from your enterprise AI assistant.
          </p>
        </div>

        <button
          type="button"
          className="new-chat-button"
          onClick={onNewChat}
        >
          New Chat
        </button>

      </div>

    </header>
  );
}

export default ChatHeader;