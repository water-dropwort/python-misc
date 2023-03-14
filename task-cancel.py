import asyncio

async def coro(n):
    try:
        for i in range(3):
            print(f"[{n}] {i}")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print(f"[{n}]task has been cancelled.")
    finally:
        print(f"[{n}]finally")

async def main():
    task = asyncio.create_task(coro(2))
    await asyncio.sleep(1)
    task.cancel()
    await task

asyncio.run(main())

# The output is below
#
# [2] 0
# [2]task has been cancelled.
# [2]finally
