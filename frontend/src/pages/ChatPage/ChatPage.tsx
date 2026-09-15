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

      <ChatHeader />


      <MessageList
        messages={messages}
      />


      {isLoading && (
        <p>
          AI Assistant is thinking...
        </p>
      )}


      {error && (
        <p>
          {error}
        </p>
      )}


      <ChatInput
        input={input}
        onInputChange={setInput}
        onSend={sendMessage}
        isLoading={isLoading}
      />

    </main>
  );
}


export default ChatPage;