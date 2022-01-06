import numpy as np

def checka(T):
    x_name = T.columns.values[0]                     # contiene il nome degli indici presenti nella prima colonna
    x_val = np.array(T[x_name].values, dtype=object) # contiene il vellore rappresentativo della prima colonna
    y_name = T.columns.values[1]                     # contiene il nome degli indici presenti nella seconda colonna
    y_val = np.array(T[y_name].values, dtype=object) # contiene il vellore rappresentativo della seconda colonna

    variable_list = ""                               # lista delle variabili in T
    z = ""                                           # vettore rappresentativo dell'unione tra x_val e y_val

    if x_name == "zero":
        y_zeros = np.count_nonzero(y_val == '0')     # nel caso iniziale la prima colonna è zero
        # se y_val è una colonna nulla allora KO
        if y_zeros == len(y_val):
            res = "KO"
        # se ci sono degli zero in y_val allora OK
        elif '0' in y_val:
            res = "OK"
        # altrimenti non ci sono zero e ho trovato un MHS
        else:
            res = "MHS"
        # se non ho KO aggiorno variable_list e z
        if res != "KO":
            variable_list = y_name
            z = y_val
    else:
        # ----------------- ??????? ----------------------------
        x_zeros = zeroCount(x_val)
        y_zeros = zeroCount(y_val)
        z = sumstr(x_val, y_val)
        z_zeros = zeroCount(z)

        if x_zeros == z_zeros or y_zeros == '0':
            res = "KO"
        elif '0' in z:
            res = "OK"
        else:
            res = "MHS"

        if res != "KO":
            variable_list = x_name + "," + y_name
            # z_name = x_name,y_name

            # print("len z indez", len(z_name))
            if not finalCheck(variable_list, z):
                res = "KO"
            '''
            if res == "MHS":

                if finalCheck(variable_list, z):
                    res = "MHS"
                else:
                    res = "KO"
            '''
            Gamma = [variable_list, z]
        else:
            Gamma = ["", ""]

    return res, variable_list, z


def finalCheck(names, z):
    count = 0
    names = str.split(names, ",")
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


# funzione che crea combina i valori dei 2 vettore rappresentativi in ingresso
def sumstr(val1, val2):

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

# funzione che restituisce il numero di '0' presenti nel vettore rappresentativo
def zeroCount(x):
    count = 0
    for elem in x:
        if elem == '0':
            count = count + 1
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
