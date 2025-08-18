import React from 'react';
import { Container, VStack, Heading, Text, Box } from '@chakra-ui/react';
import Header from '../components/Header';

const HomePage: React.FC = () => {
  return (
    <Box>
      <Header />
      <Container maxW="container.xl" py={8}>
        <VStack spacing={6} align="stretch">
          <Heading as="h1" size="xl" textAlign="center">
            Bem-vindo ao ASPG
          </Heading>
          <Text fontSize="lg" textAlign="center" color="gray.600">
            Sistema de Controle Orçamentário
          </Text>
          <Box p={6} bg="gray.50" borderRadius="md">
            <Text>
              Você está logado com sucesso! Esta é uma área protegida.
            </Text>
          </Box>
        </VStack>
      </Container>
    </Box>
  );
};

export default HomePage;