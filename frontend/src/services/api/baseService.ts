async function request<T>(
  url: string,
  options?: RequestInit
): Promise<T> {

  const response = await fetch(url, {
    ...options,

    headers: {
      "Content-Type": "application/json",
      ...options?.headers,
    },
  });

  if (!response.ok) {
    throw new Error(
      `API request failed with status ${response.status}`
    );
  }

  return response.json();
}


export const baseService = {

  get<T>(url: string): Promise<T> {
    return request<T>(url, {
      method: "GET",
    });
  },


  post<T>(
    url: string,
    body: unknown
  ): Promise<T> {

    return request<T>(url, {
      method: "POST",
      body: JSON.stringify(body),
    });
  },


  put<T>(
    url: string,
    body: unknown
  ): Promise<T> {

    return request<T>(url, {
      method: "PUT",
      body: JSON.stringify(body),
    });
  },


  delete<T>(url: string): Promise<T> {

    return request<T>(url, {
      method: "DELETE",
    });
  },
};