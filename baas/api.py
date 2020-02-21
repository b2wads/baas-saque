import json

from aiohttp import web
from asyncworker import RouteTypes

from baas.account.models import Account
from baas.app import app
from baas.http import parse_body, parse_id
from baas.services.account import AccountService


@app.route(["/accounts"], type=RouteTypes.HTTP, methods=["POST"])
@parse_body(Account)
async def create_account(acc: Account):
    raise NotImplementedError


@app.route(["/accounts"], type=RouteTypes.HTTP, methods=["GET"])
async def list_accounts(request: web.Request):
    raise NotImplementedError


@app.route(["/accounts/{acc_id}"], type=RouteTypes.HTTP, methods=["GET"])
@parse_id(str)
async def get_by_id(acc_id: str):
    acc = AccountService.get_by_id(acc_id)
    return web.json_response(acc.dict())


@app.route(
    ["/accounts/{acc_id}/debito"], type=RouteTypes.HTTP, methods=["POST"]
)
@parse_id(str)
async def debita_account(acc: Account):
    raise NotImplementedError


@app.route(
    ["/accounts/{acc_id}/credito"], type=RouteTypes.HTTP, methods=["POST"]
)
@parse_id(str)
async def credita_account(acc: Account):
    raise NotImplementedError


@app.route(["/health"], type=RouteTypes.HTTP, methods=["GET"])
async def health(req: web.Request):
    return web.json_response({"OK": True})
