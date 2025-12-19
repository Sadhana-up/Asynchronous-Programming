# import _asyncio

# async def greet():
#     return "Hello i am greeting you "

# greet()

import time ##IT BLOCKS AND WE ARE STOPPED WHEREVER WE USED THE SLEEP METHOD 
def task():
    time.sleep(5)
    print("Task is finished")

task()
print("WHIILE TASK WAS ASLEEP ")


#no blocking 

import asyncio

# async def test():
#     await asyncio.sleep(3)
#     print("Hello this is before")

# # asyncio.run(test())
# print('but this runs using the async function ')


async def test():
    await asyncio.sleep(3)
    print("Hello this is before")

async def main():
    asyncio.create_task(test())
    print('This prints immediately')
    await asyncio.sleep(4)  # give time for test() to finish

asyncio.run(main())
