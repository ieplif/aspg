import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import { Spinner, Center } from '@chakra-ui/react';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();

  console.log('🛡️ ProtectedRoute - isAuthenticated:', isAuthenticated, 'loading:', loading);
  // Log detalhado
  console.log('🛡️ ProtectedRoute executando...');
  console.log('🛡️ isAuthenticated:', isAuthenticated);
  console.log('🛡️ loading:', loading);

  // Verificar localStorage diretamente
  const token = localStorage.getItem('access_token');
  console.log('🛡️ Token no localStorage:', token ? 'EXISTE' : 'NÃO EXISTE');

  if (loading) {
    console.log('⏳ Mostrando loading...');
    return (
      <Center minH="100vh">
        <Spinner size="xl" />
      </Center>
    );
  }

  if (!isAuthenticated) {
    console.log('❌ Não autenticado, redirecionando para login...');
    return <Navigate to="/login" replace />;
  }

  console.log('✅ Autenticado, mostrando conteúdo protegido');
  return <>{children}</>;
};

export default ProtectedRoute;