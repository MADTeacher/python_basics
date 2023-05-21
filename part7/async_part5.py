import asyncio

async def task_test():
    print('Выполняем задачу')
    return (30, "-_-", [4.6, "o_O"])

async def main(loop):
    print('Объявляем задачу')
    task = loop.create_task(task_test())
    print(f'Ожидание выполнения задачи: {task}')
    return_value = await task
    print(f'Завершение задачи: {task}')
    print(f'Результат работы задачи: {return_value}')

if __name__ == "__main__":
    event_loop = asyncio.new_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()