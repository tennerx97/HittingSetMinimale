import numpy as np
import csv
import pandas as pd
import asyncio,sys
from checkmod import checka


def max(x):
    j = x.columns[-1]
    list = str.split(j, ",")
    return list[-1]


def succ(x,df):
    flag=False
    for column in df.columns:#O(n) quando è possibile meglio cambiarlo
        if flag:
            return pd.DataFrame(df[column])
        if column==x:
            flag=True

def check(x,y):
    z =np.sum([x,y],axis=0)
    #print(z)
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
    #check2(np.array([1, 1]))
    count=0
    setmhs=[]
    #check(np.array([0,0]),np.array([1,1]))
    queue = asyncio.Queue() #creo coda
    #row_matrix=len(A.index)
    #queue.get_nowait() #toglie dalla coda
    A.insert(0, "zero", 0, allow_duplicates=False)
    queue.put_nowait(A['zero'])  # inserisce nella coda
    max_A=A.shape[1] #ultimo indice del dataframe per fare il ciclo pù tardi
    #print(queue)
    while not queue.empty():
        delta=pd.DataFrame(queue.get_nowait())           # estraggo delta dalla coda
        max_delta = max(delta)
        succ_delta=(A.columns.get_loc(max_delta))+1  # calcolo l'indice numerico della colonna successiva a delta

        for column in A.columns[succ_delta:max_A]:       # per ogni colonna fra succ(max(delta)) e max(A)

            gamma=delta.join(A[column])                  # gamma dataframe unione fra delta e A[column]
            #print(gamma," gamma")
            result=checka(gamma,setmhs)
            names = result[1]  # result[1] ha il nome colonna gamma e valori
            value = result[2]
            #print("sto lavorando")

            if result[0]=="OK" and not column==A.columns[-1]:    #result [0] ha l'esito

                temp = {names: value}
                df = pd.DataFrame(temp)
                queue.put_nowait(df)
            if result[0] == "MHS":
                setmhs.append(names)
                print(names, " mhs")
                count=count+1


        #print(delta, ' elem tolto')
        #for elem=succ(max(delta)) <= max(A):
        #succ_start=succ(max(delta),A)
        #for elem in range(succ,A.columns, 1):
          #  print(A[elem])
    return count, setmhs