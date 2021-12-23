import numpy as np
import pandas as pd
import os, psutil,time,sys
from LoadMatrix import load_matrix
from MBase import MBase
from LoadMatrix2 import load_matrix2


start_time = time.time()

matrix=load_matrix()
matrixShapeInit=matrix.shape #contiene n+1 righe la prima contiene le variabili, e m colonne da 1 a m variabile
print(matrixShapeInit, "dim finale")
print(sys.getsizeof(matrix)," byte dataframe")

c=MBase(matrix)
print(c," mhs trovati")


print("--- %s seconds ---" % (time.time() - start_time))
process = psutil.Process(os.getpid())
print('Used memory: ',process.memory_info().rss,' byte')  # in bytes


