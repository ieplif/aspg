// NOTA: Este arquivo foi mantido para compatibilidade
// Para novas funcionalidades, use apiClient.ts que tem autenticação automática

const API_BASE_URL = 'http://localhost:8000';

export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

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