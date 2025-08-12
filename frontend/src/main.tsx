import React from 'react';
import ReactDOM from 'react-dom/client';
import { ChakraProvider } from '@chakra-ui/react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import LoginPage from './routes/login'; // Importe o componente LoginPage

// Defina suas rotas aqui
const router = createBrowserRouter([
  {
    path: "/login",
    element: <LoginPage />,
  },
  // Adicione outras rotas aqui conforme o projeto crescer
  {
    path: "/",
    element: <LoginPage />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ChakraProvider>
      <RouterProvider router={router} />
    </ChakraProvider>
  </React.StrictMode>,
);
