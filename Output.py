# funzione che costituisce il modulo di output: genera un file nome_matrice.txt contenente un report dettagliato
def print_report(matrix_name, count_mhs, execution_time, memory_usage,
                 matrix_shape_start, matrix_shape_final, mhs_list,dropped_name, dropped_row):
    fileName = 'output/' + matrix_name + '_output.txt'
    with open(fileName, "w") as f:
        print("======================================================================", file=f)
        print("\t\t\tMatrix " + matrix_name, file=f)
        print("======================================================================", file=f)
        print(count_mhs," mhs trovati: \n", file=f)
        min_found = False
        for elem in mhs_list:
            elem=str.split(elem,",")
            if min_found == False:
                card_min = len(elem)
                min_found = True
            print(str(elem), file=f)
            card_max = len(elem)
        print("----------------------------------------------------------------------", file=f)
        print("Card. minima degli mhs: " + str(card_min), file=f)
        print("Card. massima degli mhs: " + str(card_max), file=f)
        print("----------------------------------------------------------------------", file=f)
        print("Colonne eliminate: " + str(dropped_name), file=f)
        print("Righe eliminate: " + str(dropped_row), file=f)
        print("----------------------------------------------------------------------", file=f)
        print("Execution time: " + str(execution_time) + " seconds", file=f)
        print('Used memory: ', memory_usage, ' byte', file=f)  # in bytes
        print("Dimensione iniziale della matrice: " + str(matrix_shape_start), file=f)
        print("Dimensione finale della matrice: " + str(matrix_shape_final), file=f)
        print("----------------------------------------------------------------------", file=f)
    f.close()
