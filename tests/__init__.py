from baas.clients.account import AccountClient
from baas.models import Account, Saque


class mock_account_client:
    @classmethod
    async def _get_by_id(cls, acc_id):
        return cls.__acc_by_id[acc_id]

    @classmethod
    async def _debito(cls, account: Account, valor: int) -> Account:
        cls.__acc_by_id[account.cpf].saldo -= valor
        return cls.__acc_by_id[account.cpf]

    @classmethod
    async def _saque(cls, account: Account, saque: Saque) -> Account:
        cls.__acc_by_id[account.cpf].saldo -= saque.valor
        return cls.__acc_by_id[account.cpf]

    @classmethod
    async def _credito(cls, account: Account, valor: int) -> Account:
        cls.__acc_by_id[account.cpf].saldo += valor
        return cls.__acc_by_id[account.cpf]

    def __init__(self, origem, *extra):
        self.saved_methods = {
            AccountClient.get_by_id.__name__: AccountClient.get_by_id,
            AccountClient.saque.__name__: AccountClient.saque,
        }
        mock_account_client.__acc_by_id = dict()

        self.__acc_by_id[origem.cpf] = Account(**origem.dict())
        for e in extra:
            self.__acc_by_id[e.cpf] = Account(**e.dict())

    def __enter__(self):
        AccountClient.get_by_id = mock_account_client._get_by_id
        AccountClient.saque = mock_account_client._saque
        AccountClient.debito = mock_account_client._debito
        AccountClient.credito = mock_account_client._credito

    def __exit__(self, exc_type, exc_value, tb):
        for name, method in self.saved_methods.items():
            setattr(AccountClient, name, method)
