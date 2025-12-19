import asyncio

# def foo():
#     return 

# foo()
# print('tim')

# No need to do programs sequentially , if i use asynchronous programming in the code above , 
# i can print before even the function is executed , so tim is printed ani function chalxa (in btwn foo is waiting for sth )

# 1 CREATE A COUROUTINE : by defining a function 

async def main():
    print("hi sadhana alxi lagyo ?") 
    task = asyncio.create_task(second('hiii'))
    await task 
    print("sakko") # i want this to run while second funct is awaiting 

async def second(text):
    print(text)
    await asyncio.sleep(1)





# async is like a wrapper which creates a couroutine object , so to execute it u must AWAIT 
# print(main()) # yo execute hudeina cuz maile await garekai chuina .
# await main() aba await ta garaye teini kina chaldena vandaaa, NO EVENT LOOP . Python le ksri allow garxa ta vanda async func event loop creation thru 
asyncio.run(main()) # Event loop 

