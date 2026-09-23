import { useState } from "react";

import type { ChatMessage } from "../types/chat";
import { sendChatMessage } from "../services/chatService";

export function useChat() {

  const [messages, setMessages] =
    useState<ChatMessage[]>([]);

  const [input, setInput] =
    useState("");

  const [isLoading, setIsLoading] =
    useState(false);

  const [error, setError] =
    useState<string | null>(null);

  const [lastFailedMessage, setLastFailedMessage] =
    useState<string | null>(null);

  const sendMessage = async (
    messageOverride?: string,
    isRetry: boolean = false
  ) => {

    const messageToSend =
      messageOverride ?? input;

    if (!messageToSend.trim()) {
      return;
    }

    const currentInput = messageToSend;

    if (!isRetry) {

      const userMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "user",
        message: currentInput,
      };

      setMessages((previousMessages) => [
        ...previousMessages,
        userMessage,
      ]);

      setInput("");
    }

    setError(null);

    setIsLoading(true);

    try {

      const response = await sendChatMessage({
        user_id: "USER001",
        session_id: "FRONTEND001",
        message: currentInput,
      });

      const assistantMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "assistant",
        message: response.response,
      };

      setMessages((previousMessages) => [
        ...previousMessages,
        assistantMessage,
      ]);

      setLastFailedMessage(null);

    } catch (error) {

      console.error(
        "Failed to send chat message:",
        error
      );

      setError(
        "Unable to get a response from the AI assistant. Please try again."
      );

      setLastFailedMessage(currentInput);

    } finally {

      setIsLoading(false);

    }
  };

  const retryLastMessage = () => {

    if (!lastFailedMessage) {
      return;
    }

    sendMessage(
      lastFailedMessage,
      true
    );
  };

  return {
    messages,
    input,
    setInput,
    sendMessage,
    retryLastMessage,
    isLoading,
    error,
  };
}