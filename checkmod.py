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
    else:                                  # casi successivi al primo ciclo while
        x_zeros = zeroCount(x_val)         # conta i numeri di elementi del vettore rappresentativo che sono pari a zero
        y_zeros = zeroCount(y_val)
        z = sumstr(x_val, y_val)           # calcola l'unione dei 2 vettori rappresentativi in ingresso
        z_zeros = zeroCount(z)

        # verifico se y_zeros è già mhs, o se non ci sono differenze fra il primo vettore rapresentativo del dataframe
        # in ingresso è quello risultante calcolato in precedenza
        if x_zeros == z_zeros or y_zeros == 0:
            res = "KO"
        elif '0' in z:                             # controllo se ci sono alcuni zero nel vettore rappresentativo di z
            res = "OK"
        else:                                      # negli altri casi z è MHS
            res = "MHS"

        if res != "KO":
            variable_list = x_name + "," + y_name    # aggiorno la lista delle variabili di T

            if not finalCheck(variable_list, z):
                res = "KO"

    return res, variable_list, z

# funzione che dato un vettore rappresentativo (z), e la lista con i nomi degli indici di T (names), verifica che
# i nomi siano tutti presenti nel vettore rappresentativo
def finalCheck(names, z):
    count = 0
    names = str.split(names, ",")
    # per ogni elemento in names verifico che sia presente in z, e incremento un contatore
    for elem in names:
        if elem in z:
            count = count + 1
    if count == len(names):           # verifico che il contatore è guale alla cardinalità dei nomi
        return True
    else:
        return False


# funzione che crea un vettore rappresentativo z combinando i valori dei 2 vettori in ingresso
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
