import { baseService } from "./api/baseService";

import {
  CHAT_URL,
  CHAT_HISTORY_URL,
} from "./api/endpoints";

import type {
  ChatRequest,
  ChatResponse,
  ChatMessage,
  ChatHistoryMessage,
} from "../types/chat";

export function sendChatMessage(
  request: ChatRequest
): Promise<ChatResponse> {

  return baseService.post<ChatResponse>(
    CHAT_URL,
    request
  );
}

export async function getChatHistory(
  sessionId: string
): Promise<ChatMessage[]> {

  const history =
    await baseService.get<ChatHistoryMessage[]>(
      `${CHAT_HISTORY_URL}/${sessionId}`
    );

  return history.map((message) => ({
    id: crypto.randomUUID(),
    role: message.role,
    message: message.message,
  }));
}