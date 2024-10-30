import numpy as np
import matplotlib.pyplot as plt

# Parámetros
h = np.pi / 20  # Tamaño de paso
x_values = np.arange(1, 2 + h, h)  # Valores de x en el intervalo [1, 2] con paso h
n = len(x_values)
y = np.zeros(n)  # Vector de soluciones de y en cada punto x

# Condiciones de frontera
y_1 = 1  # y(1) = 1
y_2 = 1  # y(2) = 1

# Construcción de la matriz A y el vector b usando diferencias finitas
A = np.zeros((n, n))
b = np.zeros(n)

# Llenar la matriz A y el vector b
for i in range(1, n - 1):
    A[i, i - 1] = 1 / h**2  # coeficiente de y_(i-1)
    A[i, i] = -2 / h**2 + 1  # coeficiente de y_i
    A[i, i + 1] = 1 / h**2  # coeficiente de y_(i+1)
    b[i] = 0  # ya que no hay término independiente en la ecuación

# Aplicar las condiciones de frontera en el sistema
A[0, 0] = 1
b[0] = y_1
A[-1, -1] = 1
b[-1] = y_2

# Resolver el sistema de ecuaciones lineales
y_solution = np.linalg.solve(A, b)

# Imprimir resultados ordenados en la terminal
print("Resultados de y(x) aproximados en cada punto x:")
for xi, yi in zip(x_values, y_solution):
    print(f"x = {xi:.5f}, y = {yi:.5f}")

# Graficar la solución
plt.plot(x_values, y_solution, marker='o', color='b', label="Aproximación de y(x)")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Solución aproximada de la EDO usando diferencias finitas en el intervalo [1, 2]")
plt.legend()
plt.grid()
plt.show()
