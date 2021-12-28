import re

import numpy as np


def checka(T, setmhs):
    x_name = T.columns.values[0]
    x_val = np.array(T[x_name].values, dtype=object)
    y_name = T.columns.values[1]
    y_val = np.array(T[y_name].values, dtype=object)

    if x_name == "zero":
        y_zeros = np.count_nonzero(y_val == '0')
        if y_zeros == len(y_val):
            res = "KO"
        elif '0' in y_val:
            res = "OK"
        else:
            res = "MHS"
        if res != "KO":
            Gamma = [y_name, y_val]
        else:
            Gamma = ["", ""]

    else:
        # z = np.sum([x_val, y_val], axis=0)
        #print(x_val, y_val, "2 vett")

        x_zeros = zeroCount(x_val)
        #print("x testato")
        y_zeros = zeroCount(y_val)
        # print(y_zeros)
        z = sumstr(x_val, y_val)
        #print(z, 'è strano')
        z_zeros = zeroCount(z)

        if x_zeros == z_zeros or y_zeros == '0':
            res = "KO"
        elif '0' in z:
            res = "OK"
        else:
            res = "MHS"

        if res != "KO":
            z_name = x_name, y_name
            # print("len z indez", len(z_name))
            if res == "MHS":

                if finalCheck(z_name, z):
                    res = "MHS"
                else:
                    res = "KO"

            Gamma = [z_name, z]
        else:
            Gamma = ["", ""]
    # print(res,"res è")
    return res, Gamma


def finalCheck(names, z):
    count = 0

    for elem in names:

        if elem in z:
            count = count + 1
    # print(count, names, z, "elem da vedere in z")
    if count == len(names):
        return True
    else:
        return False


def build(val1, val2):  # creo i valori dell'array z
    for i in range(len(val1)):
        if not (val1[i] == '0' and val2[i] == '0'):
            val1[i] = '1'
    return val1


def sumstr(val1, val2):  # creo i valori dell'array z

    z = np.array(val1, dtype=object)
    for i in range(len(val1)):

        if val1[i] == '0' and val2[i] == '0':
            z[i] = '0'
        elif val1[i] == '0' and val2[i] != '0' and val2[i] != 'x':
            z[i] = val2[i]
        elif val2[i] == '0' and val1[i] != '0' and val1[i] != 'x':
            z[i] = val1[i]
        elif val1[i] == 'x' or val2[i] == 'x':
            z[i] = 'x'
        elif val2[i] != '0' and val2[i] != 'x' and val1[i] != '0' and val1[i] != 'x':
            z[i] = 'x'
    return z


def zeroCount(x):
    count = 0
    for elem in x:

        if elem == '0':
            count = count + 1
    # print(count, x, "test")
    return count


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
        if isinstance(i, (list, tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i
