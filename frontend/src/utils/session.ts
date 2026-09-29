const SESSION_STORAGE_KEY =
  "enterprise_ai_session_id";

export function getSessionId(): string {

  const existingSessionId =
    sessionStorage.getItem(
      SESSION_STORAGE_KEY
    );

  if (existingSessionId) {
    return existingSessionId;
  }

  const newSessionId =
    `SESSION-${crypto.randomUUID()}`;

  sessionStorage.setItem(
    SESSION_STORAGE_KEY,
    newSessionId
  );

  return newSessionId;
}

export function createNewSession(): string {

  const newSessionId =
    `SESSION-${crypto.randomUUID()}`;

  sessionStorage.setItem(
    SESSION_STORAGE_KEY,
    newSessionId
  );

  return newSessionId;
}