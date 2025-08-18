const API_BASE_URL = 'http://localhost:8000';

export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

// Função para obter headers de autenticação
const getAuthHeaders = () => {
  const token = localStorage.getItem('access_token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

// Cliente API genérico com autenticação
export const apiCall = async (
  endpoint: string,
  options: RequestInit = {}
): Promise<Response> => {
  const url = `${API_BASE_URL}${endpoint}`;
  
  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(getAuthHeaders() as Record<string, string>),
      ...(options.headers ? options.headers as Record<string, string> : {}),
    },
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  return response;
};

// Função de login (mantém a original)
export const loginUser = async (credentials: LoginRequest): Promise<LoginResponse> => {
  console.log('Iniciando login com:', credentials);
  
  try {
    console.log('Fazendo requisição para:', `${API_BASE_URL}/login/access-token`);
    
    const response = await fetch(`${API_BASE_URL}/login/access-token`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        username: credentials.username,
        password: credentials.password,
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log('Login bem-sucedido:', data);
    return data;
  } catch (error) {
    console.error('Erro na requisição:', error);
    throw error;
  }
};

// Exemplo de uso do apiCall para outras requisições
export const getCurrentUser = async () => {
  const response = await apiCall('/users/me');
  return response.json();
};

export const getUsers = async () => {
  const response = await apiCall('/users');
  return response.json();
};