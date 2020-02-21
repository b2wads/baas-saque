from pydantic import BaseModel


class Account(BaseModel):
    nome: str
    cpf: str
    saldo: int = 10000
