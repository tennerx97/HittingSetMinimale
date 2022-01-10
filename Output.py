import pandas as pd

from MBase import getCardinality
from configuration import *

# funzione che costituisce il modulo di output: genera un file nome_matrice.txt contenente un report dettagliato
def print_report(matrix_name, count_mhs, execution_time, memory_usage, matrix_shape_start, matrix_shape_final,
                 mhs_list,dropped_name, dropped_row, outOfTime, card_max_analizzata, pre_elab_time):
    if pre_elab_time != -1:
        fileName = 'output/' + matrix_name + '_with_pre_elab_output.txt'
    else:
        fileName = 'output/' + matrix_name + '_output.txt'
    with open(fileName, "w") as f:
        print("======================================================================", file=f)
        print("\t\t\tMatrix " + matrix_name, file=f)
        print("======================================================================", file=f)
        if outOfTime:
            print("ATTENZIONE: L'esecuzione ha superato il limite di tempo ", file=f)
            print("======================================================================", file=f)
        print(count_mhs," mhs trovati:", file=f)
        min_found = False
        for elem in mhs_list:
            if min_found == False:
                card_min = getCardinality(elem)
                min_found = True
            card_max = getCardinality(elem)
        if count_mhs > 0:
            print("\nCard. minima degli mhs: " + str(card_min), file=f)
            print("Card. massima degli mhs: " + str(card_max), file=f)
        if outOfTime:
            print("\nCard. massima analizzata: " + str(card_max_analizzata), file=f)
        print("----------------------------------------------------------------------", file=f)
        print("Dimensione iniziale della matrice: " + str(matrix_shape_start), file=f)
        print("Dimensione finale della matrice: " + str(matrix_shape_final) + "\n", file=f)
        print("Colonne eliminate: " + str(dropped_name), file=f)
        print("Righe eliminate: " + str(dropped_row), file=f)
        print("----------------------------------------------------------------------", file=f)
        print("Execution time: " + str(execution_time) + " seconds", file=f)
        print("Pre elaboration time: " + str(pre_elab_time) + " seconds", file=f)
        print('Used memory: ', memory_usage/(1024*1024), ' Megabyte', file=f)
        print("----------------------------------------------------------------------", file=f)
        if count_mhs > 0:
            print("Lista degli mhs trovati: \n", file=f)
            for elem in mhs_list:
                print(str(elem), file=f)
            print("----------------------------------------------------------------------", file=f)
    f.close()

def write_csv(matrix_name, execution_time, memory_usage, matrix_shape_start, outOfTime, pre_elab_time, preElab):
    df = pd.read_csv('mhs_results - Foglio1.csv')
    add_row = True
    execution_time = round(execution_time, 2)
    memory_usage = round(memory_usage/(1024*1024), 2)
    pre_elab_time = round(pre_elab_time, 2)
    for matrix in df['Matrix']:
        if matrix_name == matrix:
            idx = df.index[df['Matrix'] == matrix_name]
            if preElab:
                df.loc[idx, ['Execution Time pre_elab', 'Used memory pre_elab', 'Pre elaboration time',
                             'Out of Time pre_elab']] = [execution_time, memory_usage, pre_elab_time, outOfTime]
            else:
                df.loc[idx, ['Execution Time MBase', 'Used memory MBase', 'Out of Time MBase']] = \
                    [execution_time, memory_usage, outOfTime]
            add_row = False
            break
    if add_row:
        df2 = {'Matrix': matrix_name, 'Execution Time MBase': execution_time, 'Used memory MBase': memory_usage,
            'Out of Time MBase': outOfTime, 'Rows': int(matrix_shape_start[0]), 'Columns': int(matrix_shape_start[1])}
        df = df.append(df2, ignore_index=True)
    df.to_csv('mhs_results - Foglio1.csv', index=False)

def clean_csv():
    df = pd.read_csv('mhs_results - Foglio1.csv')
    df['Execution Time MBase'] = df['Execution Time MBase'].apply(lambda x: float(x.replace(',', '.')))
    df['Execution Time pre_elab'] = df['Execution Time pre_elab'].apply(lambda x: float(x.replace(',', '.')))
    df['Used memory MBase'] = df['Used memory MBase'].apply(lambda x: float(x.replace(',', '.')))
    df['Used memory pre_elab'] = df['Used memory pre_elab'].apply(lambda x: float(x.replace(',', '.')))
    df['Pre elaboration time'] = df['Pre elaboration time'].apply(lambda x: float(x.replace(',', '.')))
    df.to_csv('mhs_results - Foglio1.csv', index=False)
