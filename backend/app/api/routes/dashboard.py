from fastapi import APIRouter

router = APIRouter(tags=["dashboard"])

@router.get("/dashboard")
async def get_dashboard_data():
    # Aqui você vai retornar os dados do painel (mock ou real)
    return {"message": "Dados do dashboard"}