import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(x, y) = y(1 - 2*y)
def f(x, y):
    return y * (1 - 2 * y)

def euler_method(f, x_0, y_0, h, n_steps):
    # Inicializar arrays para almacenar valores de x e y
    x_vals = np.zeros(n_steps + 1)
    y_vals = np.zeros(n_steps + 1)
    
    # Condiciones iniciales
    x_vals[0], y_vals[0] = x_0, y_0
    
    # Iteración usando el método de Euler
    for n in range(n_steps):
        x_vals[n + 1] = x_vals[n] + h
        y_vals[n + 1] = y_vals[n] + h * f(x_vals[n], y_vals[n])
    
    return x_vals, y_vals

# Parámetros del problema
h = 0.1  # tamaño de paso
x_0 = 0  # valor inicial de x
y_0 = 0.3  # valor inicial de y
n_steps = 100  # número de pasos

# Resolver la ecuación diferencial
x_vals, y_vals = euler_method(f, x_0, y_0, h, n_steps)

# Mostrar resultados
print(f"Valor en (x_100, y_100): x_100 = {x_vals[-1]:.4f}, y_100 = {y_vals[-1]:.5f}")

# Graficar la solución
plt.plot(x_vals, y_vals, label='Método de Euler')
plt.title("Solución usando el Método de Euler")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
     