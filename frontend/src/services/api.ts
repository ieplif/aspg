const API_BASE_URL = 'http://localhost:8000';

export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export const loginUser = async (credentials: LoginRequest ): Promise<LoginResponse> => {
  console.log('Iniciando login com:', credentials);
  
  // Versão alternativa usando JSON em vez de FormData
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

    console.log('Resposta recebida:', response);
    console.log('Status:', response.status);
    console.log('Headers:', response.headers);

    if (!response.ok) {
      console.error('Resposta não OK:', response.status, response.statusText);
      const errorData = await response.json();
      console.error('Dados do erro:', errorData);
      throw new Error(errorData.detail || 'Erro no login');
    }

    console.log('Tentando fazer parse do JSON...');
    const data = await response.json();
    console.log('Dados recebidos:', data);
    
    return data;
  } catch (error) {
    console.error('Erro na requisição:', error);
    throw error;
  }
};
