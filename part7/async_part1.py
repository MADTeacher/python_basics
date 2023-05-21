import asyncio

async def test_async():
    print(await func())

async def func():
    return "Hello, async world!"

if __name__ == "__main__":
    asyncio.run(test_async())