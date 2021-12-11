import numpy as np
import re
import csv
import pandas as pd

def load_matrix2():
    whiteSpaceRegex = ";;;";
    matrix = open("./benchmarks1/74181.029.matrix", "r")
    content = matrix.read()
    content = content[:-1]  ##tolgo l'ultima riga che è vuota
    words = content.split(whiteSpaceRegex)


    words = words[5].replace(" Map ", "Map ")  ##tolgo il map all'inizio della matrice

    words = words.replace("-", "")  ##rimuovo i meno
    #words = words.replace(" \n", "\n;")  ##aggiungo un carattere separatore
    #words=re.sub(' +', ' ', words)
    words = words[:-1]  ##elimino l'ultimo spazio
    #print(words)

    cont = words.split(" \n")
    k = len(cont)
    print("stampo questo",cont)
    for i in range(len(cont)):
        cont[i] = cont[i].split(" ")
        print(len(cont[i]))

    j = len(cont[0])
    ##cont è un array di array
    mat = np.reshape(cont, (k, j))
    temp=pd.DataFrame(mat)
    temp.to_csv("log2.csv")
    print(temp.head())
    return mat