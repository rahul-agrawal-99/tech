import asyncio
import time


async def sub():
    print('sub start')
    # await asyncio.sleep(2)
    print('sub end')

async def main():
    print('main start')
    sub_task = asyncio.create_task(sub())
 # it will pause until sub_task is returned , if not await, it will not wait for sub_task and start to print 'main end'
    # await sub_task  
    # time.sleep(3)
    await asyncio.sleep(10)
    print('main end')

asyncio.run(main())



