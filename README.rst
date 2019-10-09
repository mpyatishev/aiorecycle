==========
aiorecycle
==========

.. image:: https://travis-ci.com/mpyatishev/aiorecycle.svg?branch=master
    :target: https://travis-ci.com/mpyatishev/aiorecycle
.. image:: https://codecov.io/gh/mpyatishev/aiorecycle/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mpyatishev/aiorecycle
.. image:: https://img.shields.io/pypi/v/aiorecycle.svg
    :target: https://pypi.python.org/pypi/aiorecycle


A decorator to recycle tasks in the event loop


Installation
============

.. code:: bash

   pip install aiorecycle


Usage example
=============

.. code:: python

   import asyncio

   import aiorecycle


   @aiorecycle.cycle()
   async def task():
       if asyncio.get_event_loop().time() % 2 == 0:
           print('make some periodic work')


   async def main():
       await task()
       await asyncio.sleep(3)  # emulate very important work


   if __name__ == "__main__":
      asyncio.run(main())


License
=======

``aiorecycle`` library is offered under Apache 2 license.
