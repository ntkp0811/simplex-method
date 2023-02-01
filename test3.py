from simplex import Simplex
# Matrix A is from system equation

A = [
    [1, 3, 1, 0],
    [2, 3, 0, 1]
]

B = [9, 12]

C = [-1, -2, 0, 0]


simplexAlg = Simplex(A, B, C)
simplexAlg.simplex()
# Simplex simplex(A, b, c)
#   simplex.CalculateSimplex();
