import numpy as np
import matplotlib.pyplot as plt

# Parámetros
h = 0.1
n = int(1 / h)  # Número de puntos internos
x = np.linspace(0, 1, n + 1)  # Valores de x en el dominio

# Condiciones de frontera
y0 = 2
y1 = 1

# Coeficientes de la matriz A y el vector B para el sistema Ay = B
A = np.zeros((n + 1, n + 1))
B = np.zeros(n + 1)

# Condiciones de frontera en el sistema
A[0, 0] = 1
B[0] = y0
A[-1, -1] = 1
B[-1] = y1

# Construcción del sistema de ecuaciones
for i in range(1, n):
    A[i, i-1] = 1 / h**2 - 3 / (2 * h)
    A[i, i] = -2 / h**2 + 2
    A[i, i+1] = 1 / h**2 + 3 / (2 * h)
    B[i] = 2 * x[i] + 3

# Resolución del sistema de ecuaciones
y = np.linalg.solve(A, B)

# Graficar la solución
plt.plot(x, y, label='Aproximación con diferencias finitas', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de $y\'\' = -3y\' + 2y + 2x + 3$')
plt.grid(True)
plt.legend()
plt.show()

# Imprimir resultados en la consola para cada punto
print("Valores de y en los puntos x = 0.1, 0.2, ..., 1.0:")
for i, yi in enumerate(y):
    print(f"x = {x[i]:.1f}, y = {yi:.5f}")
