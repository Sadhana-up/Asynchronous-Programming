# task1() waits for 2 seconds and prints "Task 1 done"

# task2() waits for 1 second and prints "Task 2 done"

import asyncio

async def  task1():
    await asyncio.sleep(1)
    print("Task 1 done ")

async def task2():
    await asyncio.sleep(2)

    print('task 2 done')

# async  def main():
#     ta1 = asyncio.create_task(task1())
#     await ta1
#     ta2 = asyncio.create_task(task2())
#     await ta2


async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())