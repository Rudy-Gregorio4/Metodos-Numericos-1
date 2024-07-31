import numpy as np

# Función para verificar si una matriz es simétrica
def es_simetrica(A):
    return np.allclose(A, A.T)

# Función para verificar si una matriz es positivo-definida
def es_positivo_definida(A):
    return np.all(np.linalg.eigvals(A) > 0)

# Matrices de coeficientes
A_2_1 = np.array([
    [4, 1, 1, 0, 1],
    [-1, -3, 1, 1, 0],
    [2, 1, 5, -1, -1],
    [-1, -1, -1, 4, 0],
    [0, 2, -1, 1, 4]
])

A_2_2 = np.array([
    [4, 1, -1, 1],
    [1, 4, -1, -1],
    [-1, -1, 5, 1],
    [1, -1, 1, 3]
])

A_2_3 = np.array([
    [4, -1, 0, 0, 0, 0],
    [-1, 4, -1, 0, 0, 0],
    [0, -1, 4, 0, 0, 0],
    [0, 0, 0, 4, -1, 0],
    [0, 0, 0, -1, 4, -1],
    [0, 0, 0, 0, -1, 4]
])

# Verificación de las matrices
matrices = [A_2_1, A_2_2, A_2_3]
nombres = ["Sistema 2.1", "Sistema 2.2", "Sistema 2.3"]

for i, A in enumerate(matrices):
    print(f"{nombres[i]}:")
    print("Simétrica:", es_simetrica(A))
    print("Positivo-definida:", es_positivo_definida(A))
    print()
