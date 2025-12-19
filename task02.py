#Write a program that runs an async function main() which prints:Start
# End

import asyncio
async def main():
    print('Start')
    await asyncio.sleep(1)
    print("return")

asyncio.run(main())