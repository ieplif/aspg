from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session

from app import crud
from app.api.deps import get_db, get_current_user
from app.models import User, Receita, ReceitaCreate, ReceitaUpdate, ReceitaPublic

router = APIRouter(prefix="/receitas", tags=["receitas"])


@router.get("/", response_model=List[ReceitaPublic])
def read_receitas(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    mes: Optional[int] = Query(None, ge=1, le=12),
    ano: Optional[int] = Query(None, ge=2000),
    unidade_gestora: Optional[str] = Query(None, max_length=6)
) -> List[Receita]:
    """
    Lista todas as receitas com filtros opcionais
    """
    receitas = crud.get_receitas(
        session=session,
        skip=skip,
        limit=limit,
        mes=mes,
        ano=ano,
        unidade_gestora=unidade_gestora
    )
    return receitas


@router.post("/", response_model=ReceitaPublic)
def create_receita(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    receita_in: ReceitaCreate
) -> Receita:
    """
    Criar nova receita
    """
    receita = crud.create_receita(session=session, receita_in=receita_in)
    return receita


@router.get("/{receita_id}", response_model=ReceitaPublic)
def read_receita(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    receita_id: int
) -> Receita:
    """
    Buscar receita específica por ID
    """
    receita = crud.get_receita(session=session, receita_id=receita_id)
    if not receita:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    return receita


@router.put("/{receita_id}", response_model=ReceitaPublic)
def update_receita(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    receita_id: int,
    receita_in: ReceitaUpdate
) -> Receita:
    """
    Atualizar receita
    """
    receita = crud.get_receita(session=session, receita_id=receita_id)
    if not receita:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    
    receita = crud.update_receita(
        session=session, db_receita=receita, receita_in=receita_in
    )
    return receita


@router.delete("/{receita_id}")
def delete_receita(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    receita_id: int
) -> dict:
    """
    Deletar receita
    """
    success = crud.delete_receita(session=session, receita_id=receita_id)
    if not success:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    
    return {"message": "Receita deletada com sucesso"}