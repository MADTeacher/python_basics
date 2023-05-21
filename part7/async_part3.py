import asyncio 
import functools

def callback(arg, kwarg='default'):
    print(f'Bызов callback-функции arg= {arg} ' f'kwarg = {kwarg}')

async def main(loop):
    print(f'Регистрируем callback-функцию')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='A_A')
    loop.call_soon(wrapped, "-_-") 
    await asyncio.sleep(0.2)

if __name__ == "__main__":
    event_loop = asyncio.new_event_loop() 
    try:
        print('Запуск цикла событий') 
        event_loop.run_until_complete(main(event_loop)) 
    finally:
        print('Остановка цикла событий') 
        event_loop.close()