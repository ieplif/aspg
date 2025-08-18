import { ChakraProvider } from '@chakra-ui/react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import theme from './theme';
import LoginPage from './routes/login';
import HomePage from './routes/home';

function App() {
  console.log('🚀 App component renderizando...');
  
  // Verificar autenticação diretamente no App
  const token = localStorage.getItem('access_token');
  const isAuthenticated = !!token;
  
  console.log('🚀 Token no App:', token ? 'EXISTE' : 'NÃO EXISTE');
  console.log('🚀 isAuthenticated no App:', isAuthenticated);
  
  return (
    <ChakraProvider theme={theme}>
      <BrowserRouter>
        <Routes>
          {/* Rota pública */}
          <Route path="/login" element={<LoginPage />} />
          
          {/* Rota de teste SEM proteção */}
          <Route path="/test" element={<HomePage />} />
          
          {/* Rotas com lógica direta */}
          <Route
            path="/"
            element={
              isAuthenticated ? (
                <HomePage />
              ) : (
                <Navigate to="/login" replace />
              )
            }
          />
          
          <Route
            path="/dashboard"
            element={
              isAuthenticated ? (
                <HomePage />
              ) : (
                <Navigate to="/login" replace />
              )
            }
          />
          
          {/* Redirecionar rotas não encontradas para home */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </BrowserRouter>
    </ChakraProvider>
  );
}

export default App;