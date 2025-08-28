from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session

from app import crud
from app.api.deps import get_db, get_current_user
from app.models import User, Despesa, DespesaCreate, DespesaUpdate, DespesaPublic

router = APIRouter(prefix="/despesas", tags=["despesas"])


@router.get("/", response_model=List[DespesaPublic])
def read_despesas(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    mes: Optional[int] = Query(None, ge=1, le=12),
    ano: Optional[int] = Query(None, ge=2000),
    unidade_orcamentaria: Optional[str] = Query(None, max_length=5),
    anexo: Optional[str] = Query(None, max_length=10)
) -> List[Despesa]:
    """
    Lista todas as despesas com filtros opcionais
    """
    despesas = crud.get_despesas(
        session=session,
        skip=skip,
        limit=limit,
        mes=mes,
        ano=ano,
        unidade_orcamentaria=unidade_orcamentaria,
        anexo=anexo
    )
    return despesas


@router.post("/", response_model=DespesaPublic)
def create_despesa(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    despesa_in: DespesaCreate
) -> Despesa:
    """
    Criar nova despesa
    """
    despesa = crud.create_despesa(session=session, despesa_in=despesa_in)
    return despesa


@router.get("/{despesa_id}", response_model=DespesaPublic)
def read_despesa(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    despesa_id: int
) -> Despesa:
    """
    Buscar despesa específica por ID
    """
    despesa = crud.get_despesa(session=session, despesa_id=despesa_id)
    if not despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    return despesa


@router.put("/{despesa_id}", response_model=DespesaPublic)
def update_despesa(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    despesa_id: int,
    despesa_in: DespesaUpdate
) -> Despesa:
    """
    Atualizar despesa
    """
    despesa = crud.get_despesa(session=session, despesa_id=despesa_id)
    if not despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    
    despesa = crud.update_despesa(
        session=session, db_despesa=despesa, despesa_in=despesa_in
    )
    return despesa


@router.delete("/{despesa_id}")
def delete_despesa(
    *,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    despesa_id: int
) -> dict:
    """
    Deletar despesa
    """
    success = crud.delete_despesa(session=session, despesa_id=despesa_id)
    if not success:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    
    return {"message": "Despesa deletada com sucesso"}