"""Ponto de entrada HTTP e Socket.IO do servidor."""

import socketio
from fastapi import FastAPI

api = FastAPI(title="Caô! API", version="0.1.0")


@api.get("/health")
async def health() -> dict[str, str]:
    """Sinaliza que o processo HTTP está respondendo."""
    return {"status": "ok"}


sio = socketio.AsyncServer(async_mode="asgi")
app = socketio.ASGIApp(sio, other_asgi_app=api)
