import asyncio
import threading

async def sub(num):
    print(f"[{num}] thread no is {threading.get_ident()}")
    print(f"[{num}] Hello ... ");
    await asyncio.sleep(2)
    print(f"[{num}] ... World");

async def main():
    task1 = asyncio.create_task(sub(1))
    task2 = asyncio.create_task(sub(2))
    await task1
    await task2

print("main() will be called.")
asyncio.run(main())
print("main() has been called.")

# The output is below:
#
#   main() will be called.
#   [1] thread no is 14144
#   [1] Hello ...
#   [2] thread no is 14144
#   [2] Hello ...
#   [1] ... World
#   [2] ... World
#   main() has been called.
