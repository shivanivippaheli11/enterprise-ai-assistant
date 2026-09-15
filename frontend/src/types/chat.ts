export interface ChatMessage {
  role: "user" | "assistant";
  message: string;
}

export interface ChatRequest {
  user_id: string;
  session_id: string;
  message: string;
}

export interface ChatResponse {
  response_id: string;
  session_id: string;
  response: string;
  status: "SUCCESS" | "ERROR";
  timestamp: string;
}