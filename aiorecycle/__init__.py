import asyncio
import functools


__VERSION__ = "0.0.2"


class CycleStop(Exception):
    pass


def cycle(sleep=0.1):
    def deco(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            loop = asyncio.get_running_loop()
            try:
                await func(*args, **kwargs)
            except CycleStop:
                pass
            else:
                await asyncio.sleep(sleep, loop)
                loop.create_task(wrapper(*args, **kwargs))
        return wrapper
    return deco
