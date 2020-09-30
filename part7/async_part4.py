import asyncio
import functools

def callback(future, arg):
    print(f'{arg}: результат future = {future.result()}')

async def register_callbacks(all_done):
    print('Регистрируем callback-функцию для future')
    all_done.add_done_callback(functools.partial(callback, arg=1))
    all_done.add_done_callback(functools.partial(callback, arg=2))

async def main(all_done):
    await register_callbacks(all_done)
    print('Установка результирующего значения future')
    all_done.set_result({"-_-": 10, "^_^": 20})

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        event_loop.run_until_complete(main(all_done))
    finally:
        print(f"Основной процесс: {all_done.result()}")
        event_loop.close()