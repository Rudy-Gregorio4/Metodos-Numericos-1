import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x, y) = 4 / (1 + x^2)
def f_pi_approx(x, y):
    return 4 / (1 + x**2)

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
h = 0.01  # tamaño de paso
x_0 = 0  # valor inicial de x
y_0 = 0  # valor inicial de y
x_final = 1  # valor de x hasta donde se quiere aproximar

# Número de pasos
n_steps = int(x_final / h)

# Resolver la ecuación diferencial
x_vals_pi, y_vals_pi = euler_method(f_pi_approx, x_0, y_0, h, n_steps)

# Valor aproximado de pi en y(1)
y_approx_pi = y_vals_pi[-1]

# Mostrar el valor aproximado de pi
print(f"Valor aproximado de pi: {y_approx_pi:.5f}")

# Graficar la solución
plt.plot(x_vals_pi, y_vals_pi, label="Aproximación de pi (Euler)")
plt.title("Aproximación de π usando el Método de Euler")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
