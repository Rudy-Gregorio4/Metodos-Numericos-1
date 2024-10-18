import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import sympy as sp

# 2.1. Solución analítica
x = sp.symbols('x')
y = sp.Function('y')(x)
sol_eq = sp.Eq(y.diff(x), -y + 10 * sp.sin(3 * x))
sol_analitica = sp.dsolve(sol_eq, y, ics={y.subs(x, 0): 0})
sol_analitica_func = sp.lambdify(x, sol_analitica.rhs)

# Mostrar la solución analítica
print("\n=== 2.1. Solución Analítica ===")
print(f"Solución analítica: {sol_analitica}")

# 2.3. Aproximación por el método de Euler
def euler_method(f, y0, x0, xf, h):
    n_steps = int((xf - x0) / h) + 1
    x = np.linspace(x0, xf, n_steps)
    y = np.zeros(n_steps)
    y[0] = y0
    for i in range(1, n_steps):
        y[i] = y[i-1] + h * f(x[i-1], y[i-1])
    return x, y

# Definir f(x, y) = -y + 10*sin(3*x)
def f_euler(x, y):
    return -y + 10 * np.sin(3 * x)

x_euler, y_euler = euler_method(f_euler, 0, 0, 2, 0.1)

# Mostrar la tabla de resultados de Euler
print("\n=== 2.3. Aproximación por el Método de Euler ===")
for i in range(len(x_euler)):
    print(f"x = {x_euler[i]:.2f}, y = {y_euler[i]:.5f}")

# 2.4. Interpolación polinómica (usando np.polyfit para evitar errores)
grado_polinomio = len(x_euler) - 1  # Grado máximo del polinomio (basado en puntos Euler)
coeficientes_polinomio = np.polyfit(x_euler, y_euler, grado_polinomio)  # Ajuste polinómico

# Crear el polinomio a partir de los coeficientes
polinomio = np.poly1d(coeficientes_polinomio)

# Mostrar el polinomio interpolante
print("\n=== 2.4. Polinomio Interpolante ===")
print(f"Polinomio Interpolante: {polinomio}")

# Graficar la interpolación polinómica
x_interp = np.linspace(0, 2, 100)
y_interp = polinomio(x_interp)

plt.plot(x_euler, y_euler, 'o', label='Puntos Euler')
plt.plot(x_interp, y_interp, label='Polinomio Interpolante')
plt.title('Interpolación Polinómica')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# 2.6. Comparar los resultados de Euler, la solución analítica y el polinomio interpolante
# Generar los valores de la solución analítica
x_vals = np.linspace(0, 2, 21)  # Misma cantidad de puntos que en Euler
y_vals_analitica = sol_analitica_func(x_vals)

# Generar los valores del polinomio interpolante en los mismos puntos de Euler
y_vals_polinomio = polinomio(x_vals)

# Crear la tabla comparativa
print("\n=== 2.6. Comparación de Resultados (Analítica vs Euler vs Polinomio Interpolante) ===")
print(f"{'x':>6} | {'y (Analítica)':>12} | {'y (Euler)':>12} | {'y (Polinomio)':>14} | {'Error Euler':>12} | {'Error Polinomio':>14}")
print("-" * 78)
for i in range(len(x_vals)):
    error_euler = abs(y_vals_analitica[i] - y_euler[i])
    error_polinomio = abs(y_vals_analitica[i] - y_vals_polinomio[i])
    print(f"{x_vals[i]:>6.2f} | {y_vals_analitica[i]:>12.5f} | {y_euler[i]:>12.5f} | {y_vals_polinomio[i]:>14.5f} | {error_euler:>12.5f} | {error_polinomio:>14.5f}")
