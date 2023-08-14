"""Services module."""

from aioredis import Redis


# [TODO] Service
class Service:
    # [TODO] Service > __init__
    def __init__(self, redis: Redis) -> None:
        self._redis = redis

    # [TODO] Service > process
    async def process(self) -> str:
        await self._redis.set("my-key", "value")
        return await self._redis.get("my-key")