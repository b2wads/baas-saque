from aiohttp import web
from asyncworker import RouteTypes

from baas.app import app

@app.route(["/health"], type=RouteTypes.HTTP, methods=["GET"])
async def health(req: web.Request):
    return web.json_response({"OK": True})
