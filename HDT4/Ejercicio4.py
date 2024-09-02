import numpy as np

# Datos dados
x = np.array([1.6, 2.0, 2.5, 3.2, 4.0, 4.5])
f_x = np.array([2, 8, 14, 15, 8, 2])

# Función para calcular las diferencias divididas
def diferencias_divididas(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n-j):
            coef[i,j] = (coef[i+1,j-1] - coef[i,j-1]) / (x[i+j] - x[i])
    
    return coef[0, :]  # Solo necesitamos la primera fila

# Evaluar el polinomio en un punto dado
def evaluar_newton(x, x_data, coef):
    n = len(x_data)
    p = coef[n-1]
    for k in range(1, n):
        p = coef[n-k-1] + (x - x_data[n-k-1]) * p
    return p

# Calcular diferencias divididas
coef_grado_1 = diferencias_divididas(x[:2], f_x[:2])
coef_grado_2 = diferencias_divididas(x[:3], f_x[:3])
coef_grado_3 = diferencias_divididas(x[:4], f_x[:4])

# Calcular f(2.8)
x_eval = 2.8
f_2_8_grado_1 = evaluar_newton(x_eval, x[:2], coef_grado_1)
f_2_8_grado_2 = evaluar_newton(x_eval, x[:3], coef_grado_2)
f_2_8_grado_3 = evaluar_newton(x_eval, x[:4], coef_grado_3)

# Mostrar resultados
print(f"f(2.8) con polinomio de grado 1: {f_2_8_grado_1}")
print(f"f(2.8) con polinomio de grado 2: {f_2_8_grado_2}")
print(f"f(2.8) con polinomio de grado 3: {f_2_8_grado_3}")

# Mostrar los coeficientes para entender el proceso
print("\nCoeficientes de diferencias divididas:")
print(f"Grado 1: {coef_grado_1}")
print(f"Grado 2: {coef_grado_2}")
print(f"Grado 3: {coef_grado_3}")
