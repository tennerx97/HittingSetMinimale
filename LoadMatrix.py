import time
from PreElaborazione import *
import pandas as pd
from configuration import *

def load_matrix(preElab):
    print("Carico la matrice...\n")
    matrix = open(matrix_path, "r")
    content = matrix.read()
    matrix.close()
    # pulisco la matrice inserita nella variabile content
    cleanedMatrix = clean_matrix(content)

    # k è il numero di righe della matrice
    k = len(cleanedMatrix)
    for i in range(len(cleanedMatrix)):
        cleanedMatrix[i] = cleanedMatrix[i].split(" ")

    # j è il numero di colonne della matrice
    j = len(cleanedMatrix[0]) # cleanedMatrix è la matrice

    # verifico che la matice abbia dimensione valida
    try:
        mat = np.reshape(cleanedMatrix, (k, j))
        mat_data=mat[1:,:]                              #sottomatrice con i dati
        mat_names=mat[0,:]                              #riga con i nomi degli indici
        matrix_shape_start = (k-1,j)
        dropped_columns=[]
        dropped_rows=[]
        pre_elab_time = -1
        if preElab:
            print("Eseguo le operazioni di preelaborazione...")
            start_time = time.time()
            mat_data, mat_names, dropped_columns, dropped_rows = pre_elab(mat_data, mat_names, k-1, j)
            pre_elab_time = time.time() - start_time

        # calcolo il vettore rappresentativo
        mat_data = rep_vect(mat_data,mat_names)

        # creo il dataframe sul quale lavorare
        df = pd.DataFrame(mat_data, columns=mat_names)

        return df, matrix_name, matrix_shape_start, dropped_columns, dropped_rows, pre_elab_time
    except:
        print('invalid matrix dimension')
        return None, [], 0, [], [], 0

def clean_matrix(content):
    content = content[:-1]  # tolgo l'ultima riga che è vuota
    words = content.split(whiteSpaceRegex)
    words = words[5].replace(" Map ", "")  # tolgo il map all'inizio della matrice
    words = words.replace("-", "")  # rimuovo i meno a fine riga
    words = words.replace(" \n", "\n;")  # aggiungo un carattere separatore
    words = words[:-1]  # elimino l'ultimo spazio
    return words.split("\n;")

def rep_vect(mat_data, mat_names):
    for column in range(len(mat_data[0])): # ciclo sulle colonne
        for row in range(len(mat_data)): #ciclo sulle righe
            if mat_data[row, column] == '1':
                mat_data[row, column] = mat_names[column]
    return mat_data
