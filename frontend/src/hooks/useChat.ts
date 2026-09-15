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


  const sendMessage = async () => {

    if (!input.trim()) {
      return;
    }


    const currentInput = input;


    const userMessage: ChatMessage = {
      role: "user",
      message: currentInput,
    };


    setMessages((previousMessages) => [
      ...previousMessages,
      userMessage,
    ]);


    setInput("");

    setError(null);

    setIsLoading(true);


    try {

      const response = await sendChatMessage({
        user_id: "USER001",
        session_id: "FRONTEND001",
        message: currentInput,
      });


      const assistantMessage: ChatMessage = {
        role: "assistant",
        message: response.response,
      };


      setMessages((previousMessages) => [
        ...previousMessages,
        assistantMessage,
      ]);

    } catch (error) {

      console.error(
        "Failed to send chat message:",
        error
      );

      setError(
        "Unable to get a response from the AI assistant. Please try again."
      );

    } finally {

      setIsLoading(false);

    }
  };


  return {
    messages,
    input,
    setInput,
    sendMessage,
    isLoading,
    error,
  };
}