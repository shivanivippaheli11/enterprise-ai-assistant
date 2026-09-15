import { baseService } from "./api/baseService";
import { CHAT_URL } from "./api/endpoints";

import type {
  ChatRequest,
  ChatResponse,
} from "../types/chat";


export function sendChatMessage(
  request: ChatRequest
): Promise<ChatResponse> {

  return baseService.post<ChatResponse>(
    CHAT_URL,
    request
  );
}