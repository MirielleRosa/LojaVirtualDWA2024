from fastapi import APIRouter

from dtos.novo_produto_DTO import NovoProdutoDTO
from repositories.produto_repo import ProdutoRepo


router = APIRouter(prefix="/manager")

@router.get("/obter_produtos")
async def obter_produtos():
    produtos = ProdutoRepo.obter_todos()
    return produtos

@router.post("/inserir_produtos")
async def inserir_produtos(produto: NovoProdutoDTO):
    pass
