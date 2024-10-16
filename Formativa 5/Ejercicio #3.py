import numpy as np
import matplotlib.pyplot as plt

# Función de la ecuación diferencial y' = 2y - 6
def f(x, y):
    return 2 * y - 6

# Método de Runge-Kutta de orden 4
def runge_kutta_4(x0, y0, h, x_final):
    n = int((x_final - x0) / h)
    x_vals = [x0]
    y_vals = [y0]
    x = x0
    y = y0
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = x + h
        x_vals.append(x)
        y_vals.append(y)
    return x_vals, y_vals

# Parámetros
x0 = 0  # Valor inicial de x
y0 = 1  # Valor inicial de y
h = 0.1  # Paso de integración
x_final = 1  # Valor de x donde queremos encontrar y

# Solución por Runge-Kutta de orden 4
x_vals, y_vals = runge_kutta_4(x0, y0, h, x_final)

# Gráfico de la solución aproximada
plt.plot(x_vals, y_vals, label='Aproximación Runge-Kutta 4', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución Aproximada usando Runge-Kutta de Orden 4')
plt.legend()
plt.grid(True)
plt.show()

# Mostramos el valor aproximado en x = 1
y_rk4 = y_vals[-1]
print(f"Valor aproximado de y(1): {y_rk4}")
