import numpy as np

# Definir la matriz A
A = np.array([[1, 0, -4, 1],
              [4, 5, 7, 0],
              [1, -2, 0, 3]])

# Mostrar la matriz A
print("Matriz A:")
print(A)

# 1. Calcular la norma de columnas ||A||_1
print("\n--- Cálculo de la Norma de Columnas ||A||_1 ---")
column_sums = []
for j in range(A.shape[1]):
    col_sum = sum(abs(A[i, j]) for i in range(A.shape[0]))
    column_sums.append(col_sum)
    print(f"Suma de valores absolutos en la columna {j+1}: {col_sum}")
norma_1 = max(column_sums)
print(f"Norma de columnas ||A||_1 (máximo de las sumas de columnas): {norma_1}")

# 2. Calcular la norma de Frobenius ||A||_2
print("\n--- Cálculo de la Norma de Frobenius ||A||_2 ---")
element_squares = [A[i, j]**2 for i in range(A.shape[0]) for j in range(A.shape[1])]
print("Cuadrados de cada elemento de A:", element_squares)
frobenius_sum = sum(element_squares)
norma_2 = np.sqrt(frobenius_sum)
print(f"Suma de cuadrados de todos los elementos: {frobenius_sum}")
print(f"Norma de Frobenius ||A||_2 (raíz cuadrada de la suma de cuadrados): {norma_2}")

# 3. Calcular la norma de filas ||A||_∞
print("\n--- Cálculo de la Norma de Filas ||A||_∞ ---")
row_sums = []
for i in range(A.shape[0]):
    row_sum = sum(abs(A[i, j]) for j in range(A.shape[1]))
    row_sums.append(row_sum)
    print(f"Suma de valores absolutos en la fila {i+1}: {row_sum}")
norma_inf = max(row_sums)
print(f"Norma de filas ||A||_∞ (máximo de las sumas de filas): {norma_inf}")
