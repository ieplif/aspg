import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, Button, FormControl, FormLabel, Input, Stack, Heading, Text, useToast } from '@chakra-ui/react';
import { loginUser } from '../services/api';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const toast = useToast();

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setIsLoading(true);

    try {
      const response = await loginUser({
        username: email, // O backend espera 'username', mas usamos email
        password: password,
      });

      // Armazenar o token no localStorage (em produção, considere usar httpOnly cookies )
      localStorage.setItem('access_token', response.access_token);

      toast({
        title: 'Login bem-sucedido.',
        description: 'Redirecionando para o dashboard...',
        status: 'success',
        duration: 3000,
        isClosable: true,
      });

      // Redirecionar para o dashboard ou página principal
      setTimeout(() => navigate('/dashboard'), 1000);
    } catch (error) {
      toast({
        title: 'Erro no login.',
        description: error instanceof Error ? error.message : 'Email ou senha inválidos.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Box
      minH="100vh"
      display="flex"
      alignItems="center"
      justifyContent="center"
      bg="gray.50"
    >
      <Box
        p={8}
        maxWidth="500px"
        borderWidth={1}
        borderRadius={8}
        boxShadow="lg"
        bg="white"
      >
        <Stack spacing={4} as="form" onSubmit={handleSubmit}>
          <Heading as="h1" size="xl" textAlign="center">
            ASPG - Login
          </Heading>
          <FormControl id="email">
            <FormLabel>Email</FormLabel>
            <Input
              type="email"
              placeholder="seu@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </FormControl>
          <FormControl id="password">
            <FormLabel>Senha</FormLabel>
            <Input
              type="password"
              placeholder="********"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </FormControl>
          <Button 
            type="submit" 
            colorScheme="blue" 
            size="lg" 
            fontSize="md"
            isLoading={isLoading}
            loadingText="Entrando..."
          >
            Entrar
          </Button>
          <Text textAlign="center">
            Não tem uma conta? <a href="/signup">Cadastre-se</a>
          </Text>
          <Text textAlign="center">
            Esqueceu a senha? <a href="/recover-password">Recuperar Senha</a>
          </Text>
        </Stack>
      </Box>
    </Box>
  );
};

export default LoginPage;
