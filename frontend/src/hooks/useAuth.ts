import { useState, useEffect } from 'react';

export const useAuth = () => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    console.log('🔄 useAuth useEffect executando...');
    const token = localStorage.getItem('access_token');
    console.log('🔍 Token encontrado:', token ? 'SIM' : 'NÃO');
    
    if (token) {
      console.log('✅ Token existe, definindo como autenticado');
      setIsAuthenticated(true);
    } else {
      console.log('❌ Sem token, definindo como não autenticado');
      setIsAuthenticated(false);
    }
    
    setLoading(false);
    console.log('⏰ Loading definido como false');
  }, []); // Array vazio é importante!

  const login = (token: string) => {
    console.log('✅ Fazendo login com token:', token.substring(0, 20) + '...');
    localStorage.setItem('access_token', token);
    setIsAuthenticated(true);
    console.log('✅ Estado isAuthenticated atualizado para:', true);
  };

  const logout = () => {
    console.log('🚪 Fazendo logout');
    localStorage.removeItem('access_token');
    setIsAuthenticated(false);
  };

  console.log('🎯 Hook useAuth - isAuthenticated:', isAuthenticated, 'loading:', loading);

  return {
    isAuthenticated,
    loading,
    login,
    logout,
  };
};