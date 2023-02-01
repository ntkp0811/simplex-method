from simplex import Simplex
# Matrix A is from system equation
A = [
    [1, 0, 1, 2, 1, 0, 0],
    [-2, -1, -4, 2, 0, 1, 0 ],
    [3, 1, 3, 0, 0, 0, 1],
]

B = [1, -2, 3]

C = [-1, 0, 3, -1, 0, 0, 0]


simplexAlg = Simplex(A, B, C)
simplexAlg.simplex()
# Simplex simplex(A, b, c)
#   simplex.CalculateSimplex();