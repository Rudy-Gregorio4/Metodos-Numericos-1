import numpy as np

# Definir las matrices A y B
A = np.array([[3.3, 1], [1, 3]])
B = np.array([[4, 4], [3, 5]])

# Función para calcular las normas 2 de una matriz y su inversa
def calcular_normas_y_condicionamiento(matrix):
    # Calcular la norma 2 de la matriz
    norma = np.linalg.norm(matrix, 2)
    print(f"Procedimiento: La norma ||A||_2 o ||B||_2 se calcula como el máximo valor singular de la matriz, obteniendo {norma:.4f}")
    
    # Calcular la inversa de la matriz y su norma 2
    inversa = np.linalg.inv(matrix)
    norma_inversa = np.linalg.norm(inversa, 2)
    print(f"Procedimiento: La norma ||A^-1||_2 o ||B^-1||_2 se calcula como el máximo valor singular de la inversa de la matriz, obteniendo {norma_inversa:.4f}")
    
    # Calcular el número de condicionamiento
    condicionamiento = norma * norma_inversa
    print(f"Procedimiento: El número de condicionamiento κ se calcula como el producto de ||A||_2 y ||A^-1||_2 o ||B||_2 y ||B^-1||_2. Resultado: κ = {condicionamiento:.4f}")
    
    return norma, norma_inversa, condicionamiento

# Función para calcular la pequeñez del determinante
def calcular_pequenez_determinante(matrix):
    # Calcular el determinante
    determinante = np.linalg.det(matrix)
    print(f"Procedimiento: El determinante de la matriz se calcula y se obtiene {determinante:.4f}")
    
    # Calcular la pequeñez como 1/|determinante|
    pequenez = 1 / abs(determinante) if determinante != 0 else np.inf
    print(f"Procedimiento: La pequeñez ν se calcula como 1 / |determinante|. Resultado: ν = {pequenez:.4f}")
    
    return pequenez, determinante

# Cálculos para matriz A
print("Resultados para la Matriz A:")
norma_A, norma_A_inv, cond_A = calcular_normas_y_condicionamiento(A)
pequenez_A, det_A = calcular_pequenez_determinante(A)

# Cálculos para matriz B
print("\nResultados para la Matriz B:")
norma_B, norma_B_inv, cond_B = calcular_normas_y_condicionamiento(B)
pequenez_B, det_B = calcular_pequenez_determinante(B)

# Imprimir resultados en el orden de los incisos
print("\nInciso 2.1: Normas de las matrices A y B")
print(f"Norma ||A||_2: {norma_A:.4f}")
print(f"Norma ||A^-1||_2: {norma_A_inv:.4f}")
print(f"Norma ||B||_2: {norma_B:.4f}")
print(f"Norma ||B^-1||_2: {norma_B_inv:.4f}")

print("\nInciso 2.2: Número de condicionamiento de A y B")
print(f"Número de condicionamiento κ(A): {cond_A:.4f}")
print(f"Número de condicionamiento κ(B): {cond_B:.4f}")

print("\nInciso 2.3: Pequeñez y determinante de A y B")
print(f"Pequeñez del determinante de A: {pequenez_A:.4f}")
print(f"Determinante de A: {det_A:.4f}")
print(f"Pequeñez del determinante de B: {pequenez_B:.4f}")
print(f"Determinante de B: {det_B:.4f}")

print("\nInciso 2.4: Condición de las matrices A y B")
print(f"¿Está A bien condicionada? {'Sí, debido a que κ(A) es ' + str(cond_A) if cond_A < 100 else 'No, debido a que κ(A) es ' + str(cond_A)}")
print(f"¿Está B bien condicionada? {'Sí, debido a que κ(B) es ' + str(cond_B) if cond_B < 100 else 'No, debido a que κ(B) es ' + str(cond_B)}")
