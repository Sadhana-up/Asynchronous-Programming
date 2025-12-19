import asyncio

# Write an asynchronous function say_hello() 
# that prints "Hello after 2 seconds" after waiting for 2 seconds.

async def hey():
    await asyncio.sleep(2)
    print("Hello after 2 seconds")

asyncio.run(hey())

