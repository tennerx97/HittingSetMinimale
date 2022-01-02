import os, psutil, time, sys
from LoadMatrix import load_matrix
from MBase import MBase
from Output import *
import warnings


warnings.filterwarnings("ignore")

def main():
    start_time = time.time()

    # matrix è un Dataframe contenente la matrice presa in analisi
    # matrix_name è il nome del file da cui è stata caricata la matrice
    # matrix_shape_start è la dimensione della matrice iniziale
    # dropped_name è la lista delle colonne eliminate in preprocessing
    # dropped_row è la lista delle righe eliminate in preprocessing
    matrix, matrix_name, matrix_shape_start, dropped_name, dropped_row = load_matrix()
    if matrix is None:
        return

    # matrixShapeInit contiene lo shape della matrice dopo il preprocessing
    matrixShapeInit = matrix.shape

    # stampa la memoria occupata dall'elemento matrix
    # print(sys.getsizeof(matrix)," byte dataframe")

    # count_mhs contiene il numero di mhs torvati in matrix
    # mhs_list è una lista che contiene gli mhs trovati
    count_mhs, mhs_list = MBase(matrix)

    # calcola il tempo di esecuzione
    execution_time = time.time() - start_time

    # calcola la memoria usata
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss

    # richiamo la funzione di output
    print_report(matrix_name, count_mhs, execution_time, memory_usage, matrix_shape_start, matrixShapeInit, mhs_list,
                 dropped_name, dropped_row)

if __name__ == "__main__":
    main()
