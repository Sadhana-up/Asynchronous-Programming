# Write an async function countdown(n) that prints numbers 
# from n to 1, waiting 1 second between each number.
import asyncio

async def countdown(n):
    for i in range(n,0,-1):
        print(i)
        await asyncio.sleep(1)

asyncio.run(countdown(5))