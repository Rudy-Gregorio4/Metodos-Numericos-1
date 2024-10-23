import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate  # Asegúrate de tener instalada esta librería

# Definir la función que describe el sistema de ecuaciones diferenciales
def f(t, y1, y2):
    # y1' = y2
    # y2' = 2y1 - 2y2 + e^(2t) * sin(t)
    y1_prime = y2
    y2_prime = 2 * y1 - 2 * y2 + np.exp(2 * t) * np.sin(t)
    return y1_prime, y2_prime

# Método de Euler con impresión de cada paso
def euler_method(t0, y1_0, y2_0, h, t_final):
    # Inicializar listas para almacenar los valores de t, y1, y2
    t_values = [t0]
    y1_values = [y1_0]
    y2_values = [y2_0]
    
    # Imprimir los valores iniciales
    print(f"Paso inicial: t = {t0}, y(t) = {y1_0}, y'(t) = {y2_0}")
    
    # Iterar con el método de Euler
    t = t0
    y1 = y1_0
    y2 = y2_0
    paso = 1  # Contador de pasos
    
    while t < t_final:
        y1_prime, y2_prime = f(t, y1, y2)
        
        # Actualizar valores usando el método de Euler
        y1_new = y1 + h * y1_prime
        y2_new = y2 + h * y2_prime
        t_new = t + h
        
        # Imprimir el paso actual
        print(f"Paso {paso}:")
        print(f"  t = {t_new:.2f}, y(t) = {y1_new:.5f}, y'(t) = {y2_new:.5f}")
        print(f"  y'(t) = {y1_prime:.5f}, y''(t) = {y2_prime:.5f}\n")
        
        # Almacenar los valores en las listas
        t_values.append(t_new)
        y1_values.append(y1_new)
        y2_values.append(y2_new)
        
        # Actualizar valores para la siguiente iteración
        t = t_new
        y1 = y1_new
        y2 = y2_new
        paso += 1
    
    return t_values, y1_values, y2_values

# Función para mostrar una tabla de resultados con bordes visibles (celdas)
def mostrar_tabla(t_values, y1_values, y2_values):
    data = {'t': t_values, 'y(t)': y1_values, "y'(t)": y2_values}
    tabla = pd.DataFrame(data)
    # Utilizamos tabulate para mostrar la tabla con bordes
    print("\nTabla de valores (t, y(t), y'(t)):")
    print(tabulate(tabla, headers='keys', tablefmt='grid', showindex=False))

# Parámetros iniciales
t0 = 0
y1_0 = -0.4  # y(0) = -0.4
y2_0 = -0.6  # y'(0) = -0.6
h = 0.01  # Tamaño del paso
t_final = 0.3  # Tiempo final

# Resolver usando el método de Euler
t_values, y1_values, y2_values = euler_method(t0, y1_0, y2_0, h, t_final)

# Mostrar tabla de resultados
mostrar_tabla(t_values, y1_values, y2_values)

# Imprimir los valores aproximados de y(t) y y'(t) en t = 0.3
print(f"\nValor aproximado de y(0.3): {y1_values[-1]}")
print(f"Valor aproximado de y'(0.3): {y2_values[-1]}")

# Graficar los resultados
plt.plot(t_values, y1_values, label='y(t)')
plt.plot(t_values, y2_values, label="y'(t)")
plt.xlabel('t')
plt.ylabel('y, y\'')
plt.legend()
plt.title('Método de Euler para el PVI')
plt.grid(True)
plt.show()
