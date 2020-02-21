from collections import defaultdict

from baas.models import Saque


class SaqueStorage:
    def __init__(self):
        self.__data = defaultdict(list)
        self.__by_date = defaultdict(list)

    def save(self, acc_id: str, saque: Saque):
        self.__data[acc_id].append(saque)
        self.__by_date[f"{acc_id}-{saque.data}"].append(saque)

    def get_by_acc_id(self, acc_id):
        return self.__data[acc_id]

    def get_by_date(self, acc_id, date):
        return self.__by_date[f"{acc_id}-{date}"]


class SaqueService:

    storage = SaqueStorage()

    @classmethod
    def save_saque(cls, acc_id, acc_data):
        raise NotImplementedError

    @classmethod
    def get_by_date(cls, acc_id: str, date: str):
        raise NotImplementedError

    @classmethod
    def list_saques(cls, acc_id):
        raise NotImplementedError
