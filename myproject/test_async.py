import asyncio


async def customers_long_thinking_order(num: int):
    print("syorityuu")
    await asyncio.sleep(num)
    return num,"ざるそば"


async def order():
    print("御注文は？")
    task1 = asyncio.create_task(customers_long_thinking_order(1))
    task2 = asyncio.create_task(customers_long_thinking_order(2))
    menu1 = await task1
    print(menu1)
    menu2 = await task2
    print(menu2)
asyncio.run(order())