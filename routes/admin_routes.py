from http.client import HTTPException
from fastapi import APIRouter

from dtos.excluir_produto import ExcluirProdutoDTO
from dtos.inserir_produto_dto import InserirProdutoDTO
from models.produto_model import Produto
from repositories.produto_repo import ProdutoRepo


router = APIRouter(prefix="/manager")


@router.get("/obter_produtos")
async def obter_produtos():
    produtos = ProdutoRepo.obter_todos()
    return produtos

@router.post("/inserir_produto")
async def inserir_produto(produto: InserirProdutoDTO) -> Produto:
    novo_produto = Produto(None, produto.nome, produto.preco, produto.descricao, produto.estoque)
    novo_produto = ProdutoRepo.inserir(novo_produto)
    return novo_produto

@router.delete("/excluir_produto")
async def excluir_produto(produto_dto: ExcluirProdutoDTO):
    produto_id = produto_dto.id
    sucesso = ProdutoRepo.excluir(produto_id)  
    if sucesso:
        return {"message": "Produto excluído com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")