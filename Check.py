import re

import numpy as np


def checka(T, setmhs):
    x_name = T.columns.values[0]
    x_len=len(x_name)

    x_val = np.array(T[x_name].values, dtype=int)
    y_name = T.columns.values[1]
    y_val = np.array(T[y_name].values, dtype=int)

    if x_name == "zero":
        y_zeros = np.count_nonzero(y_val == 0)
        if y_zeros == len(y_val):
            res = "KO"
        elif 0 in y_val:
            res = "OK"
        else:
            res = "MHS"
        if res != "KO":
            Gamma = [y_name, y_val]
        else:
            Gamma = ["", ""]

    else:
        z = np.sum([x_val, y_val], axis=0)
        x_zeros = np.count_nonzero(x_val == 0)
        y_zeros = np.count_nonzero(y_val == 0)
        z_zeros = np.count_nonzero(z == 0)

        if x_zeros == z_zeros or y_zeros == 0:
            res = "KO"
        elif 0 in z:
            res = "OK"
        else:
            res = "MHS"

        if res != "KO":
            z_name = x_name, y_name
            print(len(z_name),"zz")
            Gamma = [z_name, build(x_val, y_val)]
        else:
            Gamma = ["", ""]

    return res, Gamma


def build(val1, val2):  # creo i valori dell'array z
    for i in range(len(val1)):
        if not (val1[i] == 0 and val2[i] == 0):
            val1[i] = 1
    #print(np.unique(val2),val1)
    return val1



'''
z_name=set()
            z_name.add(x_name)
            z_name.add(y_name)
            z_name = [val for sublist in z_name for val in sublist]
            count=0
            notmhs=False
            for ind in setmhs:
                if len(ind)>1:
                    ind  = [val for sublist in ind for val in sublist]
                for indx in ind:
                    print(ind," ind")
                    if indx in z_name:
                        count=count+1
                    if count == len(ind):
                        notmhs=True
                        break
                count=0
            if not notmhs:
                res="MHS"
            else:
                res="KO"
'''

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i