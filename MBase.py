import numpy as np
import csv
import pandas as pd
import asyncio

def max(x):
    return x.columns[-1]

def succ(x,df):
    flag=False
    for column in df.columns:#O(n) quando è possibile meglio cambiarlo
        if flag:
            return pd.DataFrame(df[column])
        if column==x:
            flag=True

def check(x,y):
    z =np.sum([x,y],axis=0)
    print(z)
    x_zeros=np.count_nonzero(x == 0)
    y_zeros = np.count_nonzero(y == 0)
    z_zeros =np.count_nonzero(z == 0)

    if x_zeros==z_zeros or y_zeros==0:
        print("KO")
    elif 0 in z:
        print("OK")
    else:
        print("MHS")

def check2(x):
    x_zeros = np.count_nonzero(x == 0)
    if x_zeros==len(x):
        print("KO")
    elif 0 in x:
        print("OK")
    else:
        print("MHS")

def MBase(A):
    check2(np.array([1, 1]))
    check(np.array([0,0]),np.array([1,1]))
    queue = asyncio.Queue() #creo coda
    #row_matrix=len(A.index)
    #queue.get_nowait() #toglie dalla coda
    A.insert(0, "zero", 0, allow_duplicates=False)
    queue.put_nowait(A['zero'])  # inserisce nella coda

    while not queue.empty():
        delta=pd.DataFrame(queue.get_nowait())
        #print(delta, ' elem tolto')
        #for elem=succ(max(delta)) <= max(A):
        succ_start=succ(max(delta),A)
        #for elem in range(succ,A.columns, 1):
          #  print(A[elem])


















