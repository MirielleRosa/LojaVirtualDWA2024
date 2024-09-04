from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from dtos.alterar_produto_dto import AlterarProdutoDTO
from dtos.id_produto_dto import IdProdutoDTO
from dtos.inserir_produto_dto import InserirProdutoDto
from dtos.problem_detail_dto import ProblemDetailsDto
from models.produto_model import Produto
from repositories.produto_repo import ProdutoRepo


router = APIRouter(prefix="/manager")


@router.get("/obter_produtos")
async def obter_produtos():
    produtos = ProdutoRepo.obter_todos()
    return produtos

@router.post("/inserir_produto")
async def inserir_produto(inputDto: InserirProdutoDto) -> Produto:
    novo_produto = Produto(None, inputDto.nome, inputDto.preco, inputDto.descricao, inputDto.estoque)
    novo_produto = ProdutoRepo.inserir(novo_produto)
    return novo_produto

@router.post("/excluir_produto")
async def excluir_produto(inputDto: IdProdutoDTO):
    if ProdutoRepo.excluir(inputDto.id_produto): return None
    pb = ProblemDetailsDto("int", f"O produto com id {inputDto.id_produto} não foi encontrado.", "value_not_found", ["body", "id_produto"])
    return JSONResponse(pb.to_dict(), status_code=404)


@router.get("/obter_produto_por_id")
async def obter_produto_por_id(inputDto: IdProdutoDTO = Depends()):
    if ProdutoRepo.obter_um(inputDto.id_produto): return None
    pb = ProblemDetailsDto("int", f"O produto com id {inputDto.id_produto} não foi encontrado.", "value_not_found", ["body", "id_produto"])
    return JSONResponse(pb.to_dict(), status_code=404)

@router.post("/alterar_produto")
async def alterar_produto(inputDto: AlterarProdutoDTO) -> Produto:
    produto = Produto(inputDto.id, inputDto.nome, inputDto.preco, inputDto.descricao, inputDto.estoque)
    
    if ProdutoRepo.alterar(produto): return None
    pb = ProblemDetailsDto("int", f"O produto com id {inputDto.id_produto} não foi encontrado.", "value_not_found", ["body", "id"])
    return JSONResponse(pb.to_dict(), status_code=404)