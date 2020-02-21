from baas.account.models import Account


class AccountStorage:
    def __init__(self):
        self.__data = dict()

    def save(self, acc_id: str, acc_data: Account):
        self.__data[acc_id] = acc_data

    def get_by_id(self, acc_id):
        return self.__data[acc_id]


class AccountService:

    storage = AccountStorage()

    @classmethod
    def save_account(cls, acc_id, acc_data):
        raise NotImplementedError

    @classmethod
    def get_by_id(cls, acc_id):
        return cls.storage.get_by_id(acc_id)
