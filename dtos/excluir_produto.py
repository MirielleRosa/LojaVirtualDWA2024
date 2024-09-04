from pydantic import BaseModel, field_validator

class ExcluirProdutoDTO(BaseModel):
    id: int  
    
    @field_validator("id")
    def validar_id(cls, v):
        if v <= 0:
            raise ValueError("ID do produto deve ser um número maior que zero.")
        return v