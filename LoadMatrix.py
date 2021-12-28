import numpy as np
import csv
from PreElaborazione import pre
import pandas as pd
def load_matrix():
    whiteSpaceRegex = ";;;";
    matrix = open("./benchmarks2/74L85.002.matrix", "r")
    #74L85.000.matrix  matrice facile
    #c2670.039.matrix va senza map c5315.260.matrix
    content = matrix.read()
    matrix.close()
    content = content[:-1]  ##tolgo l'ultima riga che è vuota
    words = content.split(whiteSpaceRegex)
    words = words[5].replace(" Map ", "")  ##tolgo il map all'inizio della matrice

    words = words.replace("-", "")  ##rimuovo i meno
    words = words.replace(" \n", "\n;")  ##aggiungo un carattere separatore

    words = words[:-1]  ##elimino l'ultimo spazio

    cont = words.split("\n;")
    k = len(cont)
    for i in range(len(cont)):
        cont[i] = cont[i].split(" ")

    j = len(cont[0])
    ##cont è un array di array
    print("ciao")

    try:

        mat = np.reshape(cont, (k, j))
        mat_data=mat[1:,:]                              #sottomatrice con i dati
        mat_names=mat[0,:]                              #riga con i nomi degli indici
        print(k-1,j, "dim iniziale")
        #mat_data,mat_names = pre(mat_data,mat_names,k-1,j)
        mat_data=rep_vect(mat_data,mat_names)

        print(mat_data, "new daat")

        temp = pd.DataFrame(mat_data,columns=mat_names) #creo il dataframe sul quale lavorare

        #temp.to_csv("log.csv")
        #print(temp.head())
        return temp
    except:
        print('invalid matrix dimension')
        return 0

def rep_vect(mat_data,mat_names):
    new_collen = len(mat_data[0])
    newl = len(mat_data)
    for i in range(new_collen):
        for row in range(newl):
            if mat_data[row, i] == '1':
                mat_data[row, i] = mat_names[i]
    return mat_data
