"""Verificação básica da aplicação ASGI montada."""

import asyncio

from httpx import ASGITransport, AsyncClient

from cao_backend.app import app


def test_health_is_available_through_the_combined_asgi_app() -> None:
    async def request_health():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://testserver"
        ) as client:
            return await client.get("/health")

    response = asyncio.run(request_health())
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
