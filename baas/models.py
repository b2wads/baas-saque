from typing import Optional

from pydantic import BaseModel


class Account(BaseModel):
    nome: Optional[str]
    cpf: Optional[str]
    saldo: Optional[int]


class Saque(BaseModel):
    valor: int
    account: Optional[Account]
