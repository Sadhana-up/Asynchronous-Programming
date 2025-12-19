
# Simulate fetching user data asynchronously:
# Fetch data for users [1, 2, 3] concurrently and print the results.

import asyncio 

async def fetch_user(user_id):
    await asyncio.sleep(2)
    return f"User {user_id} data"

async def main():
    t =await  asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3)

    )
    

    for n in t :
        print(n)


asyncio.run(main())