from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlmodel import Field, SQLModel

# ===== USER MODELS (existentes) =====
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserRegister(UserCreate):
    pass

class UserUpdate(UserBase):
    password: Optional[str] = None

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

class UserPublic(UserBase):
    id: int

class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int

# ===== RECEITA MODELS (novos) =====
class ReceitaBase(SQLModel):
    """Modelo base para Receita"""
    unidade_gestora: str = Field(max_length=6, description="Código UG de 6 dígitos")
    unidade_orcamentaria: str = Field(max_length=5, description="Código UO de 5 dígitos")
    natureza_receita_codigo: str = Field(max_length=10, description="Código NR de 10 dígitos")
    natureza_receita_especificacao: str = Field(max_length=500, description="Especificação da Natureza da Receita")
    fonte_recursos: str = Field(max_length=7, description="Código FR de 7 dígitos")
    previsao_inicial: Decimal = Field(max_digits=15, decimal_places=2, description="Valor da previsão inicial")
    mes: int = Field(ge=1, le=12, description="Mês (1-12)")
    ano: Optional[int] = Field(default=None, description="Ano (opcional)")

class Receita(ReceitaBase, table=True):
    """Modelo da tabela Receita"""
    __tablename__ = "receitas"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class ReceitaCreate(ReceitaBase):
    """Schema para criar receita"""
    pass

class ReceitaUpdate(SQLModel):
    """Schema para atualizar receita"""
    unidade_gestora: Optional[str] = Field(None, max_length=6)
    unidade_orcamentaria: Optional[str] = Field(None, max_length=5)
    natureza_receita_codigo: Optional[str] = Field(None, max_length=10)
    natureza_receita_especificacao: Optional[str] = Field(None, max_length=500)
    fonte_recursos: Optional[str] = Field(None, max_length=7)
    previsao_inicial: Optional[Decimal] = Field(None, max_digits=15, decimal_places=2)
    mes: Optional[int] = Field(None, ge=1, le=12)
    ano: Optional[int] = None

class ReceitaPublic(ReceitaBase):
    """Schema público da receita (resposta da API)"""
    id: int
    created_at: datetime
    updated_at: datetime


# ===== DESPESA MODELS (novos) =====
class DespesaBase(SQLModel):
    """Modelo base para Despesa"""
    unidade_orcamentaria: str = Field(max_length=5, description="Código UO de 5 dígitos")
    anexo: str = Field(max_length=10, description="Anexo (algarismos romanos)")
    programa_trabalho: str = Field(max_length=6, description="Código PT de 6 dígitos")
    subelemento: str = Field(max_length=8, description="Código Subelemento de 8 dígitos")
    descricao: str = Field(max_length=1000, description="Descrição da despesa")
    processo: str = Field(max_length=100, description="Número do processo")
    favorecido: str = Field(max_length=500, description="Nome do favorecido")
    valor: Decimal = Field(max_digits=15, decimal_places=2, description="Valor da despesa")
    mes: int = Field(ge=1, le=12, description="Mês (1-12)")
    ano: Optional[int] = Field(default=None, description="Ano (opcional)")

class Despesa(DespesaBase, table=True):
    """Modelo da tabela Despesa"""
    __tablename__ = "despesas"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class DespesaCreate(DespesaBase):
    """Schema para criar despesa"""
    pass

class DespesaUpdate(SQLModel):
    """Schema para atualizar despesa"""
    unidade_orcamentaria: Optional[str] = Field(None, max_length=5)
    anexo: Optional[str] = Field(None, max_length=10)
    programa_trabalho: Optional[str] = Field(None, max_length=6)
    subelemento: Optional[str] = Field(None, max_length=8)
    descricao: Optional[str] = Field(None, max_length=1000)
    processo: Optional[str] = Field(None, max_length=100)
    favorecido: Optional[str] = Field(None, max_length=500)
    valor: Optional[Decimal] = Field(None, max_digits=15, decimal_places=2)
    mes: Optional[int] = Field(None, ge=1, le=12)
    ano: Optional[int] = None

class DespesaPublic(DespesaBase):
    """Schema público da despesa (resposta da API)"""
    id: int
    created_at: datetime
    updated_at: datetime

# ===== SHARED MODELS =====
class Message(SQLModel):
    message: str

class NewPassword(SQLModel):
    token: str
    new_password: str

class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(SQLModel):
    sub: Optional[int] = None