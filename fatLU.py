import numpy as np
import scipy.linalg

def lu_decomposition(A):
    P, L, U = scipy.linalg.lu(A)
    return P, L, U

def solve_lu(L, U, b):
    # Soluciona L*y = b
    y = np.linalg.solve(L, b)
    # Soluciona U*x = y
    x = np.linalg.solve(U, y)
    return x

# Exemplo de uso
A = np.array([[3, 1, 6], [2, 1, 2], [1, 1, 1]], dtype=float)
b = np.array([12, 6, 3], dtype=float)

P, L, U = lu_decomposition(A)
print("Matriz P (permutações):")
print(P)
print("Matriz L:")
print(L)
print("Matriz U:")
print(U)

x = solve_lu(L, U, b)
print("Solução do sistema:")
print(x)
