import asyncio
async def fetch_data():
    print('START FETCHING')
    await asyncio.sleep(2)
    print("fetching completed")
    return {"data":1}

async def print_nums():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_nums())

    value = await task1 # assign value in value variable after task1s completion 
    print(value)
    await task2

asyncio.run(main())
