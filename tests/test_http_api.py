from http import HTTPStatus

from asynctest import TestCase
from asyncworker.testing import HttpClientContext

from baas.account.models import Account
from baas.api import app
from baas.services.account import AccountService


class AccountAPITest(TestCase):
    async def test_get_account_id(self):
        account = Account(nome="Dalton Barreto", cpf="1234")
        async with HttpClientContext(app) as client:
            AccountService.storage.save(account.cpf, account)

            acc_resp = await client.get("/accounts/1234")
            acc_data = await acc_resp.json()
            self.assertEqual(HTTPStatus.OK, acc_resp.status)
            self.assertEqual({**account.dict(), "saldo": 10000}, acc_data)

    async def test_health(self):
        async with HttpClientContext(app) as client:
            resp = await client.get("/health")
            data = await resp.json()
            self.assertEqual({"OK": True}, data)
