import numpy as np

# Definición de los sistemas de ecuaciones
# Sistema 6.1
A_6_1 = np.array([
    [-0.10, 1.00],
    [0.11, -1.00]
])
b_6_1 = np.array([-2.0, 2.1])

# Sistema 6.2
A_6_2 = np.array([
    [-0.10, 1.00],
    [0.11, -1.00]
])
b_6_2 = np.array([-2.00, 2.14])

# Función para resolver el sistema y obtener los resultados por sección
def resolver_sistema(A, b):
    # Sección 6.1 y 6.2: Solución del sistema
    try:
        solucion = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        solucion = None
    
    # Sección 6.3: Número de condición de la matriz
    condicion = np.linalg.cond(A, p='fro')
    
    # Sección 6.4: Determinante y valores propios de la matriz de coeficientes
    determinante = np.linalg.det(A)
    autovalores = np.linalg.eigvals(A)
    
    return solucion, condicion, determinante, autovalores

# Resolución de ambos sistemas
solucion_6_1, condicion_6_1, determinante_6_1, autovalores_6_1 = resolver_sistema(A_6_1, b_6_1)
solucion_6_2, condicion_6_2, determinante_6_2, autovalores_6_2 = resolver_sistema(A_6_2, b_6_2)

# Impresión de los resultados por sección
print("Resultados del ejercicio 6")

# Sección 6.1 y 6.2: Solución del sistema de ecuaciones
print("\nSección 6.1 y 6.2: Solución del sistema")
print("Solución para el Sistema 6.1 (x, y):", solucion_6_1 if solucion_6_1 is not None else "No tiene solución única.")
print("Solución para el Sistema 6.2 (x, y):", solucion_6_2 if solucion_6_2 is not None else "No tiene solución única.")

# Sección 6.3: Número de condición de la matriz
print("\nSección 6.3: Análisis de condición del sistema")
print("Número de condición (κ) para el Sistema 6.1:", condicion_6_1)
print("Número de condición (κ) para el Sistema 6.2:", condicion_6_2)

# Interpretación de la condición del sistema
print("Interpretación:")
if condicion_6_1 < 100:
    print("Sistema 6.1 está bien condicionado.")
else:
    print("Sistema 6.1 está mal condicionado (sensible a variaciones en los coeficientes).")
    
if condicion_6_2 < 100:
    print("Sistema 6.2 está bien condicionado.")
else:
    print("Sistema 6.2 está mal condicionado (sensible a variaciones en los coeficientes).")

# Sección 6.4: Determinante y valores propios de la matriz de coeficientes
print("\nSección 6.4: Determinante y valores propios de la matriz de coeficientes")
print("Determinante de la matriz para el Sistema 6.1:", determinante_6_1)
print("Determinante de la matriz para el Sistema 6.2:", determinante_6_2)
print("Valores propios de la matriz de coeficientes para el Sistema 6.1:", autovalores_6_1)
print("Valores propios de la matriz de coeficientes para el Sistema 6.2:", autovalores_6_2)

# Interpretación adicional
print("\nInterpretación:")
print("- Un determinante cercano a cero en cualquiera de los sistemas indica que podría ser difícil de resolver de manera estable.")
print("- Valores propios pequeños sugieren que la matriz es casi singular, lo cual contribuye a un alto número de condición.")
