import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
h = 0.05  # paso de discretización
x0, xn = 1, 2  # intervalo
N = int((xn - x0) / h)  # número de puntos internos
x_values = np.linspace(x0, xn, N + 1)  # valores de x_i

# Condiciones de frontera
y0 = -0.5
yN = np.log(2)

# Inicialización de la matriz A y el vector B para el sistema Ax = B
A = np.zeros((N+1, N+1))  # matriz de coeficientes
B = np.zeros(N+1)  # vector independiente

# Aplicamos las condiciones de frontera en el sistema
A[0, 0] = 1
B[0] = y0  # y(1) = -0.5
A[N, N] = 1
B[N] = yN  # y(2) = ln(2)

# Llenado de la matriz A y el vector B usando diferencias finitas
for i in range(1, N):
    xi = x_values[i]
    
    # Coeficientes para y_{i-1}, y_i, y_{i+1} en la ecuación de diferencias finitas
    A[i, i-1] = 1 / h**2 - 2 / (2 * h * xi)  # coeficiente de y_{i-1}
    A[i, i] = -2 / h**2 + 2 / xi**2          # coeficiente de y_i
    A[i, i+1] = 1 / h**2 + 2 / (2 * h * xi)  # coeficiente de y_{i+1}
    
    # Término independiente correspondiente
    B[i] = -2 * np.log(xi) / xi**2

# Resolución del sistema de ecuaciones lineales
y_values = np.linalg.solve(A, B)

# Mostrar resultados en la terminal
print("Matriz de coeficientes A:")
print(A)
print("\nVector independiente B:")
print(B)
print("\nResultados aproximados de y en cada x_i:")
for i in range(N + 1):
    print(f"x = {x_values[i]:.2f}, y ≈ {y_values[i]:.5f}")

# Visualizar los resultados en una gráfica
plt.plot(x_values, y_values, marker='o', color='b', label="Solución aproximada")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solución aproximada de la EDO usando diferencias finitas")
plt.legend()
plt.grid()
plt.show()