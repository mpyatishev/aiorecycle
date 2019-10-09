import asyncio

import aiorecycle
import pytest


@pytest.mark.asyncio
async def test_task_recycles(event_loop):
    """
    it should schedule the task in the event loop
    """

    class Worker:
        count = 0

        @aiorecycle.cycle()
        async def some_task(self):
            self.count += 1

    worker = Worker()
    task = event_loop.create_task(worker.some_task())
    await asyncio.sleep(0.3)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass

    assert worker.count != 0


@pytest.mark.asyncio
async def test_task_stops_by_signal(event_loop):
    """
    it should stop the task by the signal
    """

    @aiorecycle.cycle()
    async def some_task():
        raise aiorecycle.CycleStop()

    task = event_loop.create_task(some_task())
    await task
