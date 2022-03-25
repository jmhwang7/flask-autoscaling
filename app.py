import aioredis
import asyncio

async def main():
    redis = aioredis.from_url("redis://red-c8sf3jd0maldij14587g:6379")
    await redis.set("my-key", "value")
    value = await redis.get("my-key")
    print(value)


if __name__ == "__main__":
    asyncio.run(main())
