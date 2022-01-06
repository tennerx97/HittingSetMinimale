#74L85.000.matrix  matrice facile
#c2670.039.matrix va senza map c5315.260.matrix

#matrix_path = "./benchmarks2/74L85.002.matrix" # (4, 33)
#matrix_path = "./benchmarks2/74181.025.matrix" # (10, 65)
matrix_path = "./benchmarks2/c432.010.matrix" # (10, 160)
#matrix_path = "./benchmarks2/c432.044.matrix" # (35, 160)

matrix_name = matrix_path[14:23]
whiteSpaceRegex = ";;;";
timeLimit = 60  # limite di tempo massimo per ricercare mhs
executePreElab = True