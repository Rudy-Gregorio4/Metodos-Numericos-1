import numpy as np
import pandas as pd

# Definir las matrices A y B para los ejercicios 2 y 3
A_ej2 = np.array([[3.3, 1], [1, 3]])
B_ej2 = np.array([[4, 4], [3, 5]])
A_ej3 = np.array([[1, 0.22], [4, 1]])
B_ej3 = np.array([[3, 5], [-2, 2]])

# Función para calcular norma 2, norma infinito y números de condicionamiento
def calcular_normas(matrix):
    # Calcular norma 2 y su inversa
    norma_2 = np.linalg.norm(matrix, 2)
    norma_2_inv = np.linalg.norm(np.linalg.inv(matrix), 2)
    cond_2 = norma_2 * norma_2_inv
    
    # Calcular norma infinito y su inversa
    norma_inf = np.linalg.norm(matrix, np.inf)
    norma_inf_inv = np.linalg.norm(np.linalg.inv(matrix), np.inf)
    cond_inf = norma_inf * norma_inf_inv
    
    return norma_2, norma_2_inv, cond_2, norma_inf, norma_inf_inv, cond_inf

# Crear una lista para almacenar los resultados
resultados = []

# Calcular y almacenar resultados para cada matriz en los ejercicios 2 y 3
for nombre, matriz in [("A (Ej2)", A_ej2), ("B (Ej2)", B_ej2), ("A (Ej3)", A_ej3), ("B (Ej3)", B_ej3)]:
    norma_2, norma_2_inv, cond_2, norma_inf, norma_inf_inv, cond_inf = calcular_normas(matriz)
    resultados.append({
        "Matriz": nombre,
        "Norma 2": norma_2,
        "Norma 2 Inversa": norma_2_inv,
        "Condición (Norma 2)": cond_2,
        "Norma ∞": norma_inf,
        "Norma ∞ Inversa": norma_inf_inv,
        "Condición (Norma ∞)": cond_inf,
        "Bien Condicionada (Norma 2)": "Sí" if cond_2 < 100 else "No",
        "Bien Condicionada (Norma ∞)": "Sí" if cond_inf < 100 else "No"
    })

# Convertir los resultados en un DataFrame de pandas para mejor visualización
df_resultados = pd.DataFrame(resultados)

# Mostrar la tabla de resultados
print("Comparación de resultados entre Norma 2 y Norma ∞:")
print(df_resultados)
