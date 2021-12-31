import numpy as np

def pre_elab(mat, name, n, m):
    # togli_righe restituisce la nuova matrice e la lista delle righe rimosse
    mat, dropped_row = togli_righe(mat, n, m)

    # togli_colonne restituisce la nuova matrice, la lista delle colonne rimaste e la lista delle colonne rimosse
    mat, name, dropped_name = togli_colonne(mat, name, m)

    return mat, name, dropped_name, dropped_row


def togli_righe(mat, rows, columns):
    removedRows = [] # contiene le righe da rimuovere
    for i in range(rows):
        for j in range(i + 1, rows):
            res = checkSub(mat[i, :], mat[j, :], columns)
            if res == 2:
                removedRows.append(j)
                print("La riga ",j," contiene la riga ", i)
            elif res == 1 or res == 0:
                print("La riga ",i," contiene la riga ", j)
                removedRows.append(i)
    removedRows = np.array(removedRows)
    removedRows = np.unique(removedRows) # elimino i duplicati
    for i in reversed(removedRows):
        mat = np.delete(mat, i, axis=0)

    return mat, removedRows

# ritorna -1 se non c'è sottoinsieme
# ritorna 1 se il primo array ingloba il secondo
# ritorna 2 se il secondo array ingloba il primo
# ritorna 0 se i due array sono uguali
def checkSub(riga1, riga2, columns):
    res = 0
    for i in range(columns):
        if riga1[i] == '1' and riga2[i] == '1':
            res = res
        elif riga1[i] == '1' and riga2[i] == '0':
            if res == 2:
                res = -1
                break
            else:
                res = 1
        elif riga1[i] == '0' and riga2[i] == '1':
            if res == 1:
                res = -1
                break
            else:
                res = 2
    return res


def togli_colonne(mat, name, columns):
    rows = len(mat) # ricalcolo rows perchè potrebbe essere minore
    newname = [] # lista che contiene i nomi delle colonne che rimangono
    dropped_name = [] # lista che contiene i nomi delle colonne che vengono rimosse
    newmat = [] # nuova matrice

    zeros = np.zeros(rows).astype(int).astype(str)
    for i in range(columns):
        if (mat[:, i] == zeros).all():
            dropped_name.append(name[i])
            print("La colonna ", name[i], " è stata rimossa perchè nulla")
        else:
            newname.append(name[i])
            newmat.append(mat[:, i])
    newmat = np.array(newmat)

    return newmat.T, newname, dropped_name
