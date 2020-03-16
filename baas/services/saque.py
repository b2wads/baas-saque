from collections import defaultdict
from typing import List

from baas.clients.account import AccountClient
from baas.models import Account, Saque


class SaqueStorage:
    def __init__(self):
        self.clear()

    def clear(self):
        self.__data = defaultdict(list)

    def save(self, acc_id: str, saque: Saque):
        self.__data[acc_id].append(saque)

    def get_by_acc_id(self, acc_id: str):
        return self.__data[acc_id]


class SaqueService:

    storage = SaqueStorage()

    @classmethod
    async def save_saque(cls, acc_id: str, saque: Saque) -> Saque:
        raise NotImplementedError

    @classmethod
    def list_by_acc_id(cls, acc_id: str) -> List[Saque]:
        raise NotImplementedError
