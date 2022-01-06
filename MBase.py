import pandas as pd
import asyncio, time
from checkmod import checka
from configuration import *

def getCardinality(elem):
    return len(str.split(elem, ","))

def max(x):
    j = x.columns[-1]
    list = str.split(j, ",")
    return list[-1]

def MBase(A):
    count = 0  # contatore degli mhs
    setmhs = []  # set degli mhs
    queue = asyncio.Queue()  # creo la coda
    A.insert(0, "zero", 0, allow_duplicates=False)
    queue.put_nowait(A['zero'])  # inserisce nella coda
    max_A = A.shape[1]  # ultimo indice del dataframe per fare il ciclo pù tardi
    start_time = time.time()
    outOfTime = False   # indica se il tempo di ricerca ha superato il limite temporale
    while not queue.empty() and time.time() - start_time <= timeLimit:

        delta = pd.DataFrame(queue.get_nowait())  # estraggo delta dalla coda
        max_delta = max(delta)
        succ_delta = (A.columns.get_loc(max_delta)) + 1  # calcolo l'indice numerico della colonna successiva a delta

        for column in A.columns[succ_delta:max_A]:  # per ogni colonna fra succ(max(delta)) e max(A)

            gamma = delta.join(A[column])  # gamma dataframe unione fra delta e A[column]

            # result è OK, KO, MHS
            # names contiene il nome della colonna MHS, vuoto se non è MHS
            # value contiene il vettore rappresentativo di gamma aggiornato
            result, names, value = checka(gamma)

            # se gamma è OK e la colonna non è l'ultima aggiungo in coda
            if result == "OK" and not column == A.columns[-1]:
                temp = {names: value}
                df = pd.DataFrame(temp)
                queue.put_nowait(df)
            # se gamma è MHS aggiungo al set degli mhs
            elif result == "MHS":
                setmhs.append(names)
                print(names, " mhs")
                count = count + 1

    searchTime=time.time() - start_time #tempo di ricerca
    card_max_analizzata = -1
    if searchTime >= timeLimit:
        outOfTime = True
        card_max_analizzata = getCardinality(str(gamma.columns[0]+','+gamma.columns[1]))

    return count, setmhs, outOfTime, card_max_analizzata
