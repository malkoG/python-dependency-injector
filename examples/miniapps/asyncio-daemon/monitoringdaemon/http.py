"""Http client module."""

from aiohttp import ClientSession, ClientTimeout, ClientResponse


# [TODO] HttpClient
class HttpClient:

    # [TODO] HttpClient > request
    async def request(self, method: str, url: str, timeout: int) -> ClientResponse:
        async with ClientSession(timeout=ClientTimeout(timeout)) as session:
            async with session.request(method, url) as response:
                return response
