from pydantic import BaseModel


class Account(BaseModel):
    nome: str
    cpf: str


class Saque(BaseModel):
    data: str
    valor: int
    account: Account
