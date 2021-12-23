import numpy
import numpy as np


def pre(mat, name, n, m):
    mat = togliRighe(mat, n, m)
    mat, name = togliColonne(mat, name, m)

    return mat, name


def togliRighe(mat, n, m):
    newmat = []
    h = 0
    for i in range(n):
        # print(mat[i, :], " riga ",i)
        for j in range(i + 1, n):
            if j != i:
                res = checkSub(mat[i, :], mat[j, :], m)
                if res == 2:
                    #mat = np.delete(newmat, i, axis=0)
                    newmat.append(i)
                elif res == 1 or res == 0:
                    #mat = np.delete(mat, j, axis=0)
                    newmat.append(j)
        h = h + 1
    newmat = np.array(newmat)
    newmat=np.unique(newmat)
    for i in reversed(newmat):
        mat = np.delete(mat, i, axis=0)

    print(newmat, "new less rig")
    return mat


def checkSub(a, b,
             m):  # ritorna -1 se non c'è sottoinsieme, 1 se il primo array ingloba il secondo, 2 se il secondo array ingloba il primo/ theta(m)
    res = 0
    for i in range(m):
        if a[i] == '1' and b[i] == '1':
            res = res
        elif a[i] == '1' and b[i] == '0':
            if res == 2:
                res = -1
                break
            else:
                res = 1
        elif a[i] == '0' and b[i] == '1':
            if res == 1:
                res = -1
                break
            else:
                res = 2
    return res


def togliColonne(mat, name, m):  # ricalcolo n perchè potrebbe essere minore
    n = len(mat)
    newname = []
    newmat = []
    # print(mat[:,1])

    for i in range(m):  # colonna
        rem = 0
        # print(i)
        for j in range(n):  # riga
            # print(j, i)

            if mat[j, i] == "0":
                rem = rem + 1
            # print(rem)

        if rem != n:
            # print(mat[:, i], i)
            newname.append(name[i])
            newmat.append(mat[:, i])

    newmat = np.array(newmat)
    print(newname, newmat.T, newmat.T.shape, " forma")
    return newmat.T, newname
