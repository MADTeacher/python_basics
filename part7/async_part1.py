import asyncio

async def test_async():
    print(await func())

async def func():
    return "Hello, async world!"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_async())