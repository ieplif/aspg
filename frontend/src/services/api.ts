const API_BASE_URL = 'http://localhost:8000'; // URL do seu backend FastAPI

export interface LoginRequest {
  username: string; // Note que o FastAPI OAuth2 espera 'username', não 'email'
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export const loginUser = async (credentials: LoginRequest ): Promise<LoginResponse> => {
  const formData = new FormData();
  formData.append('username', credentials.username);
  formData.append('password', credentials.password);

  const response = await fetch(`${API_BASE_URL}/login/access-token`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Erro no login');
  }

  return response.json();
};

export const createUser = async (userData: {
  email: string;
  password: string;
  full_name?: string;
}) => {
  const response = await fetch(`${API_BASE_URL}/users/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Erro ao criar usuário');
  }

  return response.json();
};
