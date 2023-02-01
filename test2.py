from simplex import Simplex
# Matrix A is from system equation

A = [
    [6, -4, -5, 1, 0, 0, 0],
    [1, 2, 1, 0, 0, 1, 0],
    [-3, 2, 1, 0, -1, 0, 1]
]

B = [20, 8, 8]

C = [0, 0, 0, 0, 0, 1, 1]


simplexAlg = Simplex(A, B, C)
simplexAlg.simplex()
# Simplex simplex(A, b, c)
#   simplex.CalculateSimplex();
