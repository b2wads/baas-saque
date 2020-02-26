from typing import List

from aiohttp import web
from asyncworker import RouteTypes

from baas.app import app
from baas.http import parse_body, parse_id
from baas.models import Saque
from baas.services.saque import SaqueService


@app.route(["/saques/{acc_id}"], type=RouteTypes.HTTP, methods=["POST"])
@parse_body(Saque)
@parse_id(str)
async def saque(acc_id: str, saque: Saque):
    raise NotImplementedError


@app.route(["/saques/{acc_id}"], type=RouteTypes.HTTP, methods=["GET"])
@parse_id(str)
async def lista_saques(req: web.Request) -> List[Saque]:
    raise NotImplementedError


@app.route(["/health"], type=RouteTypes.HTTP, methods=["GET"])
async def health():
    return web.json_response({"OK": True})
