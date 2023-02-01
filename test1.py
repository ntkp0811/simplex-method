from simplex import Simplex
# Matrix A is from system equation

A = [
    [2, 3, 1, 1, 0, 0],
    [4, 1, 2, 0, 1, 0],
    [3, 4, 2, 0, 0, 1]
]

B = [5, 11, 8]

C = [-5, -4, -3, 0, 0, 0]


simplexAlg = Simplex(A, B, C)
simplexAlg.simplex()
# Simplex simplex(A, b, c)
#   simplex.CalculateSimplex();
