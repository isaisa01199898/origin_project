
import time
import random
import math
import _thread



import uasyncio as asyncio
from al.hub import al_asyncio

from al.hub import radio_block

def varHandle(key, val):
    globals()[key].set(val)

radio_block.register(None, varHandle)

from al.blocks import timer
async def task_0():
    timer.resetTimer()
    while not (10 < timer.getTimer()):
        await asyncio.sleep(0.01)
        await radio_block.group(35)
        await radio_block.sendMessage('Hello')


al_asyncio.regist(task_0)

_thread.stack_size(8*1024)
al_asyncio.run()
