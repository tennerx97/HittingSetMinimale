import numpy as np
import pandas as pd
import os, psutil,time,sys
from LoadMatrix import load_matrix
from MBase import MBase
from LoadMatrix2 import load_matrix2


def print_report(matrix_name, count_mhs, execution_time, memory_usage, matrix_shape_start, matrix_shape_final, mhs_list):
    fileName = 'output/' + matrix_name + '_output.txt'
    with open(fileName, "w") as f:
        print("======================================================================", file=f)
        print("\t\t\tMatrix " + matrix_name, file=f)
        print("======================================================================", file=f)
        print(count_mhs," mhs trovati: \n", file=f)
        min_found = False
        for elem in mhs_list:
            if isinstance(elem, str):
                print(elem, file=f)
                card_min = 1
                min_found = True
                card_max = 1
            else:
                if min_found == False:
                    card_min = len(elem)
                    min_found = True
                print(str(elem), file=f)
                card_max = len(elem)
        print("----------------------------------------------------------------------", file=f)
        print("Cardinalità minima degli mhs: " + str(card_min), file=f)
        print("Cardinalità massima degli mhs: " + str(card_max), file=f)
        print("----------------------------------------------------------------------", file=f)
        print("Execution time: " + str(execution_time) + " seconds", file=f)
        print('Used memory: ', memory_usage, ' byte', file=f)  # in bytes
        print("Dimensione iniziale della matrice: " + str(matrix_shape_start), file=f)
        print("Dimensione finale della matrice: " + str(matrix_shape_final), file=f)
        print("----------------------------------------------------------------------", file=f)
    f.close()

start_time = time.time()

matrix, matrix_name, matrix_shape_start = load_matrix()
matrixShapeInit = matrix.shape #contiene n+1 righe la prima contiene le variabili, e m colonne da 1 a m variabile
# print(sys.getsizeof(matrix)," byte dataframe")

# count_mhs contiene il numero di mhs torvati in matrix
count_mhs, mhs_list = MBase(matrix)

# calcola il tempo di esecuzione
execution_time = time.time() - start_time

# calcola la memoria usata
process = psutil.Process(os.getpid())
memory_usage = process.memory_info().rss

# richiamo la funzione di output
print_report(matrix_name, count_mhs, execution_time, memory_usage, matrix_shape_start, matrixShapeInit, mhs_list)



