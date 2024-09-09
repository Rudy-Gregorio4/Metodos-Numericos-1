import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.interpolate import CubicSpline

# Datos
x_i = np.array([0, 1, 2, 3])
y_i = np.array([1, 2, 33, 244])

# Definir variable simbólica para x
x = sp.Symbol('x')

# Función para calcular el polinomio de Lagrange simbólicamente
def lagrange_polynomial_symbolic(x, x_i, y_i):
    n = len(x_i)
    P = 0
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_i[j]) / (x_i[i] - x_i[j])
        P += y_i[i] * L_i
    return sp.simplify(P)

# Calcular el polinomio de Lagrange simbólico
P_sym = lagrange_polynomial_symbolic(x, x_i, y_i)

# Mostrar el polinomio de Lagrange
print(f"El polinomio interpolante de Lagrange es: \n{P_sym}")

# Convertir el polinomio simbólico en una función numérica
P_numeric = sp.lambdify(x, P_sym, modules=['numpy'])

# Graficar el polinomio de Lagrange
x_vals = np.linspace(0, 3, 100)
P_vals = P_numeric(x_vals)

# Estimar el valor de y cuando x = 2.7
x_est = 2.7
y_est_lagrange = P_numeric(x_est)

# ----------- Trazador cúbico -----------
# Construir el trazador cúbico utilizando los datos
cs = CubicSpline(x_i, y_i)

# Estimar el valor de y cuando x = 2.7 utilizando el trazador cúbico
y_est_spline = cs(x_est)

# Generar valores de y para graficar el trazador cúbico
y_vals_spline = cs(x_vals)

# ----------- Gráfica -----------
plt.plot(x_vals, P_vals, label='Polinomio de Lagrange')
plt.plot(x_vals, y_vals_spline, '--', label='Trazador cúbico')
plt.scatter(x_i, y_i, color='red', label='Puntos dados')
plt.scatter([x_est], [y_est_lagrange], color='green', label=f'Lagrange en x=2.7: {y_est_lagrange:.2f}')
plt.scatter([x_est], [y_est_spline], color='blue', label=f'Trazador cúbico en x=2.7: {y_est_spline:.2f}')
plt.title('Polinomio de Lagrange vs Trazador Cúbico')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir los valores estimados
print(f"El valor estimado de y para x = 2.7 con Lagrange es: {y_est_lagrange}")
print(f"El valor estimado de y para x = 2.7 con el trazador cúbico es: {y_est_spline}")
