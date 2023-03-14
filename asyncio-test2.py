import asyncio

async def func(n, t):
    for i in range(5):
        print(f"[{n}] {i}")
        if t:
            await asyncio.sleep(1)

async def main1():
    task1 = asyncio.create_task(func(1, True))
    task2 = asyncio.create_task(func(2, False))
    await task1
    await task2

async def main2():
    await func(1,True)
    await func(2,False)

async def main3():
    await asyncio.create_task(func(1, True))
    await asyncio.create_task(func(2, False))

print("=== main1 ===")
asyncio.run(main1())
print("=== main2===")
asyncio.run(main2())
print("=== main3===")
asyncio.run(main3())
