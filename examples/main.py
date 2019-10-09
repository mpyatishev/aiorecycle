import asyncio

import aiorecycle


@aiorecycle.cycle()
async def task():
    time = int(asyncio.get_event_loop().time())
    if time % 2 == 0:
        print(f'{time}: do some periodic work in task')


class Worker:
    @aiorecycle.cycle(sleep=1)
    async def task(self):
        time = int(asyncio.get_event_loop().time())
        if time % 3 == 0:
            print(f'{time}: do some periodic work in Worker.task')

    @aiorecycle.cycle()
    async def task3(self):
        time = int(asyncio.get_event_loop().time())
        if time % 5 == 0:
            print('it`s time to die')
            raise aiorecycle.CycleStop()  # stop task by itself
        print(f'{time}: do some periodic work in Worker.task3')


async def main():
    asyncio.create_task(Worker().task())
    asyncio.create_task(Worker().task3())

    task2 = asyncio.create_task(task())

    await asyncio.sleep(3)

    task2.cancel()  # stop task from outside
    try:
        await task2
    except asyncio.CancelledError:
        print("task2 canceled")

    await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
