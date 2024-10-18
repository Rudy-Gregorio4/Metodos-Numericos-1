import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from scipy.interpolate import lagrange
from scipy.optimize import fsolve

# Definir la función f(t, y) de la ecuación diferencial
def f(t, y):
    return -(y + 1) * (y + 3)

# Método de Runge-Kutta de 4to orden (RK4)
def runge_kutta_4(f, t0, y0, t_final, h):
    # Número de pasos
    n = int((t_final - t0) / h)
    
    # Inicializar listas de t e y
    t_vals = np.linspace(t0, t_final, n+1)
    y_vals = np.zeros(n+1)
    y_vals[0] = y0  # Condición inicial

    # Iterar usando RK4
    for i in range(n):
        t_n = t_vals[i]
        y_n = y_vals[i]
        
        k1 = h * f(t_n, y_n)
        k2 = h * f(t_n + h/2, y_n + k1/2)
        k3 = h * f(t_n + h/2, y_n + k2/2)
        k4 = h * f(t_n + h, y_n + k3)
        
        y_vals[i+1] = y_n + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t_vals, y_vals

# Crear el polinomio interpolante
def polinomio_interpolante(t_vals, y_vals):
    # Crear el polinomio usando la interpolación de Lagrange
    polinomio = lagrange(t_vals, y_vals)
    return polinomio

# Encontrar las raíces positivas del polinomio interpolante
def encontrar_raices(polinomio, intervalo):
    # Convertir el polinomio a una representación que permita encontrar las raíces
    coeficientes = Polynomial(polinomio).coef
    raices = np.roots(coeficientes)
    
    # Filtrar solo las raíces reales y positivas en el intervalo
    raices_reales = raices[np.isreal(raices)].real
    raices_positivas = [r for r in raices_reales if intervalo[0] <= r <= intervalo[1] and r > 0]
    return raices_positivas

# Valores iniciales
t0 = 0
y0 = -2
t_final = 2
h = 0.1  # Tamaño de paso

# Llamar al método de RK4
t_vals_rk4, y_vals_rk4 = runge_kutta_4(f, t0, y0, t_final, h)

# Crear el polinomio interpolante
polinomio = polinomio_interpolante(t_vals_rk4, y_vals_rk4)

# Encontrar las raíces positivas en el intervalo [0, 2]
raices_positivas = encontrar_raices(polinomio, [0, 2])

# Mostrar los resultados en una forma visualmente "bonita"
print("\n" + "="*50)
print(f"Solución aproximada con el método de Runge-Kutta 4 (h = {h}):\n")
print(f"{'t':^10} | {'y(t)':^10}")
print("-"*50)
for t, y in zip(t_vals_rk4, y_vals_rk4):
    print(f"{t:^10.2f} | {y:^10.5f}")
print("="*50)

# Mostrar el polinomio interpolante
print("\nPolinomio interpolante (forma aproximada):")
print(np.poly1d(polinomio))

# Mostrar las raíces positivas
print("\nRaíces positivas del polinomio en el intervalo [0, 2]:")
if len(raices_positivas) > 0:
    for i, raiz in enumerate(raices_positivas, 1):
        print(f"Raíz {i}: {raiz:.5f}")
else:
    print("No se encontraron raíces positivas en el intervalo.")

# Graficar la solución
plt.plot(t_vals_rk4, y_vals_rk4, 'o-', label='Solución RK4', color='blue')
t_interpolado = np.linspace(t0, t_final, 100)
y_interpolado = np.polyval(polinomio, t_interpolado)
plt.plot(t_interpolado, y_interpolado, '--', label='Polinomio interpolante', color='green')
plt.title('Solución de la EDO con Runge-Kutta 4 y Polinomio Interpolante')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
