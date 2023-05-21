import asyncio

async def first_function():
    print("first_function start")
    for it in range(7):
        await asyncio.sleep(1.2)
        print(f"first_function {it}")

async def second_function():
    print("second_function start")
    for it in range(10):
        await asyncio.sleep(0.9)
        print(f"second_function {it}")

async def main():
    await asyncio.gather(first_function(), second_function())

if __name__ == "__main__":
    asyncio.run(main())