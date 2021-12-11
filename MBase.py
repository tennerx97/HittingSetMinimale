import numpy as np
import csv
import pandas as pd
import asyncio


def MBase(A):

    queue = asyncio.Queue() #creo coda
    queue.put_nowait(0) #inserisce nella coda
    queue.put_nowait(4)  # inserisce nella coda
    #queue.get_nowait() #toglie dalla coda
    while not queue.empty():
        a=queue.get_nowait()
        print(a, ' elem tolto')



