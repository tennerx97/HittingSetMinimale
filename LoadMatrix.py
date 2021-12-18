import numpy as np
import csv
import pandas as pd
def load_matrix():
    whiteSpaceRegex = ";;;";
    matrix = open("./benchmarks2/74L85.000.matrix", "r")
    #c2670.039.matrix va senza map c5315.260.matrix
    content = matrix.read()
    #print(content)
    content = content[:-1]  ##tolgo l'ultima riga che è vuota
    #print(content)
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

    try:

        mat = np.reshape(cont, (k, j))
        mat_data=mat[1:,:]
        mat_names=mat[0,:]
        temp = pd.DataFrame(mat_data,columns=mat_names)
        temp.to_csv("log.csv")
        #print(temp.head())
        return temp
    except:
        print('invalid matrix dimension')
        return 0

