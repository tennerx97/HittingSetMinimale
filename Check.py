import numpy as np

def checka(T):
    x_name=T.columns.values[0]
    x_val=np.array(T[x_name].values,dtype=int)
    y_name = T.columns.values[1]
    y_val=np.array(T[y_name].values,dtype=int)
    res=""

    if x_name=="zero":
        y_zeros = np.count_nonzero(y_val == 0)
        if y_zeros == len(y_val):
            res="KO"
        elif 0 in y_val:
            res="OK"
        else:
            res="MHS"
        if res !="KO":
            Gamma=[y_name,y_val]
        else:
            Gamma=["",""]

    else:
        z = np.sum([x_val, y_val], axis=0)
        x_zeros = np.count_nonzero(x_val == 0)
        y_zeros = np.count_nonzero(y_val == 0)
        z_zeros = np.count_nonzero(z == 0)

        if x_zeros == z_zeros or y_zeros == 0:
            res="KO"
        elif 0 in z:
            res="OK"
        else:
            res="MHS"
        if res !="KO":
            z_name=x_name,y_name
            Gamma=[z_name,build(x_val,y_val)]
        else:
            Gamma=["",""]

    return res,Gamma

def build(val1,val2):                        #creo i valori dell'array z
    for i in range(len(val1)):
        if val1[i]==0 and val2[i]==0:
            val1[i]=0
        else:
            val1[i]=1

    print(val1,"test or")
    return val1

