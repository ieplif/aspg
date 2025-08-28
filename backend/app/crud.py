from typing import Any, Dict, Optional, Union, List

from sqlmodel import Session, select

from app.core.security import get_password_hash, verify_password
from app.models import User, UserCreate, UserUpdate
from app.models import Receita, ReceitaCreate, ReceitaUpdate, Despesa, DespesaCreate, DespesaUpdate


def get_user_by_email(*, session: Session, email: str) -> Optional[User]:
    return session.exec(select(User).where(User.email == email)).first()

# (adicionar esta função se não existir)

def get_user(*, session: Session, user_id: int) -> User | None:
    """Buscar usuário por ID"""
    return session.get(User, user_id)


def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_user = User.model_validate(user_create, update={"hashed_password": get_password_hash(user_create.password)})
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def authenticate(
    *, session: Session, email: str, password: str
) -> Optional[User]:
    user = get_user_by_email(session=session, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def update_user(
    *, session: Session, user: User, user_update: Union[UserUpdate, Dict[str, Any]]
) -> User:
    for key, value in user_update.items():
        if key == "password":
            user.hashed_password = get_password_hash(value)
        else:
            setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def create_receita(*, session: Session, receita_in: ReceitaCreate) -> Receita:
    """Criar nova receita"""
    receita = Receita.model_validate(receita_in)
    session.add(receita)
    session.commit()
    session.refresh(receita)
    return receita


def get_receita(*, session: Session, receita_id: int) -> Optional[Receita]:
    """Buscar receita por ID"""
    return session.get(Receita, receita_id)


def get_receitas(
    *, 
    session: Session, 
    skip: int = 0, 
    limit: int = 100,
    mes: Optional[int] = None,
    ano: Optional[int] = None,
    unidade_gestora: Optional[str] = None
) -> List[Receita]:
    """Listar receitas com filtros opcionais"""
    statement = select(Receita)
    
    if mes:
        statement = statement.where(Receita.mes == mes)
    if ano:
        statement = statement.where(Receita.ano == ano)
    if unidade_gestora:
        statement = statement.where(Receita.unidade_gestora == unidade_gestora)
    
    statement = statement.offset(skip).limit(limit)
    return session.exec(statement).all()


def update_receita(
    *, 
    session: Session, 
    db_receita: Receita, 
    receita_in: ReceitaUpdate
) -> Receita:
    """Atualizar receita"""
    receita_data = receita_in.model_dump(exclude_unset=True)
    db_receita.sqlmodel_update(receita_data)
    session.add(db_receita)
    session.commit()
    session.refresh(db_receita)
    return db_receita


def delete_receita(*, session: Session, receita_id: int) -> bool:
    """Deletar receita"""
    receita = session.get(Receita, receita_id)
    if receita:
        session.delete(receita)
        session.commit()
        return True
    return False


# ===== DESPESA CRUD =====
def create_despesa(*, session: Session, despesa_in: DespesaCreate) -> Despesa:
    """Criar nova despesa"""
    despesa = Despesa.model_validate(despesa_in)
    session.add(despesa)
    session.commit()
    session.refresh(despesa)
    return despesa


def get_despesa(*, session: Session, despesa_id: int) -> Optional[Despesa]:
    """Buscar despesa por ID"""
    return session.get(Despesa, despesa_id)


def get_despesas(
    *, 
    session: Session, 
    skip: int = 0, 
    limit: int = 100,
    mes: Optional[int] = None,
    ano: Optional[int] = None,
    unidade_orcamentaria: Optional[str] = None,
    anexo: Optional[str] = None
) -> List[Despesa]:
    """Listar despesas com filtros opcionais"""
    statement = select(Despesa)
    
    if mes:
        statement = statement.where(Despesa.mes == mes)
    if ano:
        statement = statement.where(Despesa.ano == ano)
    if unidade_orcamentaria:
        statement = statement.where(Despesa.unidade_orcamentaria == unidade_orcamentaria)
    if anexo:
        statement = statement.where(Despesa.anexo == anexo)
    
    statement = statement.offset(skip).limit(limit)
    return session.exec(statement).all()


def update_despesa(
    *, 
    session: Session, 
    db_despesa: Despesa, 
    despesa_in: DespesaUpdate
) -> Despesa:
    """Atualizar despesa"""
    despesa_data = despesa_in.model_dump(exclude_unset=True)
    db_despesa.sqlmodel_update(despesa_data)
    session.add(db_despesa)
    session.commit()
    session.refresh(db_despesa)
    return db_despesa


def delete_despesa(*, session: Session, despesa_id: int) -> bool:
    """Deletar despesa"""
    despesa = session.get(Despesa, despesa_id)
    if despesa:
        session.delete(despesa)
        session.commit()
        return True
    return False