import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator

# Definición de la función f(x)
def f(x):
    return 1 / (1 + x**2)

# Selección de 11 puntos equidistantes en el intervalo [-5, 5]
x_values = np.linspace(-5, 5, 11)  # 11 puntos (polinomio de grado 10)
y_values = f(x_values)             # Evaluamos f(x) en esos puntos

# Interpolación usando un polinomio de grado 10
interpolador = BarycentricInterpolator(x_values, y_values)

# Evaluamos el polinomio interpolado en x = 2.8
x_eval = 2.8
f_interpolado = interpolador(x_eval)

# Valor real de la función en x = 2.8
f_real = f(x_eval)

# Imprimimos los resultados
print(f"Valor interpolado de f(2.8): {f_interpolado}")
print(f"Valor real de f(2.8): {f_real}")

# Visualización (opcional) para ver la diferencia entre el polinomio interpolado y la función real
x_plot = np.linspace(-5, 5, 500)
y_plot = f(x_plot)
y_interp_plot = interpolador(x_plot)

plt.plot(x_plot, y_plot, label="Función Real f(x)")
plt.plot(x_plot, y_interp_plot, '--', label="Polinomio Interpolado")
plt.scatter(x_values, y_values, color='red', label="Puntos de Interpolación")
plt.scatter([x_eval], [f_interpolado], color='green', label=f"f({x_eval}) Interpolado")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Interpolación Polinómica de Grado 10")
plt.grid(True)
plt.show()
