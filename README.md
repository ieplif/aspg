# 🚀 Fullstack Template - React + FastAPI + PostgreSQL

Template completo para aplicações web fullstack com autenticação JWT.

## 📋 Stack Tecnológica

### Backend
- **FastAPI** + **Uvicorn** 
- **SQLModel** (SQLAlchemy + Pydantic)
- **PostgreSQL**
- **JWT Authentication**
- **Poetry** para dependências

### Frontend  
- **React** + **TypeScript**
- **Vite** para build
- **Chakra UI** para componentes
- **React Router** para navegação

### DevOps
- **Docker** + **docker-compose**
- **pgAdmin** para administração
- **Nginx** para servir frontend

## 🚀 Setup Rápido

```bash
# 1. Clonar o template
git clone <NOVO-REPO-URL> meu-novo-projeto
cd meu-novo-projeto

# 2. Configurar ambiente
cp .env.example .env

# 3. Subir containers
docker-compose up --build -d

# 4. Acessar aplicação
# Frontend: http://localhost:5173
# Backend: http://localhost:8000  
# pgAdmin: http://localhost:5050
```

## 🔧 Customização

### Para novo projeto:
1. Alterar nomes nos arquivos `docker-compose.yml`
2. Atualizar `backend/pyproject.toml`
3. Atualizar `frontend/package.json`
4. Configurar variáveis no `.env`

## 🔐 Login Padrão
- **Email:** test@example.com
- **Senha:** testpassword

## 📚 Estrutura do Projeto
```
projeto/
├── backend/          # FastAPI + SQLModel
├── frontend/         # React + TypeScript  
├── docker-compose.yml
└── .env
```

## 🎯 Funcionalidades Incluídas
- ✅ Autenticação JWT completa
- ✅ Proteção de rotas
- ✅ Persistência de login
- ✅ Interface responsiva com Chakra UI
- ✅ API RESTful com FastAPI
- ✅ Banco PostgreSQL com pgAdmin
- ✅ Containerização completa com Docker