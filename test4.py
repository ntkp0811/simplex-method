from simplex import Simplex
# Matrix A is from system equation
A = [
    [3, -1, -2, 1, 0, 0, 0],
    [-2, -4, 4, 0, 1, 0, 0],
    [1, 0, -2, 0, 0, 1, 0],
    [-2, 1, 1, 0, 0, 0, 1]
]

B = [7, 3, 4, 8]

C = [1, -3, 3, 0, 0, 0, 0]


simplexAlg = Simplex(A, B, C)
simplexAlg.simplex()
# Simplex simplex(A, b, c)
#   simplex.CalculateSimplex();
