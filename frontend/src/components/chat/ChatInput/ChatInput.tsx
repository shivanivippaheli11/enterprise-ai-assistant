import "./ChatInput.css";


interface ChatInputProps {
  input: string;
  onInputChange: (value: string) => void;
  onSend: () => void;
  isLoading: boolean;
}


function ChatInput({
  input,
  onInputChange,
  onSend,
  isLoading,
}: ChatInputProps) {

  const handleKeyDown = (
    event: React.KeyboardEvent<HTMLInputElement>
  ) => {

    if (
      event.key === "Enter" &&
      !isLoading
    ) {
      onSend();
    }
  };


  return (
    <section className="chat-input">

      <input
        type="text"
        value={input}
        onChange={(event) =>
          onInputChange(event.target.value)
        }
        onKeyDown={handleKeyDown}
        placeholder={
          isLoading
            ? "AI Assistant is responding..."
            : "Type your message..."
        }
        disabled={isLoading}
      />


      <button
        onClick={onSend}
        disabled={isLoading}
      >
        {isLoading ? "Sending..." : "Send"}
      </button>

    </section>
  );
}


export default ChatInput;