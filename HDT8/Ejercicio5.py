import numpy as np

# Definición de la matriz de entrada
matriz_principal = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
])

# Sección 5.1 - Cálculo del número de condición utilizando la norma de Frobenius
print("Sección 5.1 - Cálculo del número de condición (κ):")
norma_matriz_principal = np.linalg.norm(matriz_principal, 'fro')
try:
    inversa_matriz = np.linalg.inv(matriz_principal)
    norma_inversa_matriz = np.linalg.norm(inversa_matriz, 'fro')
    numero_condicion = norma_matriz_principal * norma_inversa_matriz
    print(f"El número de condición de la matriz es: {numero_condicion:.4f}")
except np.linalg.LinAlgError:
    numero_condicion = None  # La matriz no es invertible
    print("La matriz no es invertible, por lo tanto, no tiene número de condición.")

print("\n")  # Espacio para separar las secciones

# Sección 5.2 - Cálculo del determinante de la matriz
print("Sección 5.2 - Determinante de la matriz:")
determinante_matriz = np.linalg.det(matriz_principal)
print(f"El determinante de la matriz es: {determinante_matriz:.4e}")

print("\n")

# Sección 5.3 - Cálculo de la magnitud (valor absoluto) del determinante de la matriz
print("Sección 5.3 - Magnitud del determinante (pequeñez del determinante):")
magnitud_determinante_matriz = abs(determinante_matriz)
print(f"La magnitud del determinante de la matriz es: {magnitud_determinante_matriz:.4e}")

print("\n")

# Sección 5.4 - Cálculo de los valores propios (autovalores) de la matriz
print("Sección 5.4 - Autovalores y análisis de la condición:")
autovalores = np.linalg.eigvals(matriz_principal)
print("Los autovalores de la matriz son:")
for i, autovalor in enumerate(autovalores, start=1):
    print(f"  Autovalor {i}: {autovalor:.4f}")

# Análisis adicional (opcional): Relación entre el número de condición y los autovalores
print("\nAnálisis: Si los autovalores están muy cerca de cero, esto puede indicar que la matriz es mal condicionada.")
print("Esto significa que la matriz es sensible a pequeñas perturbaciones, lo cual se refleja en un alto número de condición.")
