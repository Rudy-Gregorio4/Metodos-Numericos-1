import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.interpolate import interp1d

# Función que imprime el número del ejercicio
def mostrar_ejercicio(num_ejercicio):
    print(f"\n--{num_ejercicio}--")

# Método predictor-corrector de Heun
def metodo_heun(ecuacion, t_vals, valor_inicial, paso):
    soluciones = [valor_inicial]
    
    for i in range(1, len(t_vals)):
        t = t_vals[i-1]
        y_actual = soluciones[-1]
        
        # Predictor usando método de Euler
        prediccion = y_actual + paso * ecuacion(t, y_actual)
        
        # Corrector usando Heun
        correccion = y_actual + (paso / 2) * (ecuacion(t, y_actual) + ecuacion(t_vals[i], prediccion))
        
        soluciones.append(correccion)
        
    return soluciones

# Ejercicio 3.1: Solución analítica
mostrar_ejercicio("3.1: Solución analítica")

x = sp.symbols('x')
y = sp.Function('y')
ec_diff = sp.Eq(y(x).diff(x), -y(x) + 10 * sp.sin(3 * x))

solucion_exacta = sp.dsolve(ec_diff, y(x), ics={y(0): 0})
print(f"Solución exacta: {solucion_exacta}")

# Convertir la solución simbólica a una función para evaluar numéricamente
funcion_sol = sp.lambdify(x, solucion_exacta.rhs)

# Graficar solución analítica
x_valores = np.linspace(0, 2, 100)
y_valores = funcion_sol(x_valores)

plt.plot(x_valores, y_valores, label='Solución analítica', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución exacta para la EDO')
plt.grid(True)
plt.legend()
plt.show()

# Ejercicio 3.2: Raíces de la solución analítica
mostrar_ejercicio("3.2: Raíces de la solución analítica")

# Encontrar raíces de la solución analítica
raices_analiticas = sp.solve(solucion_exacta.rhs, x)

# Filtrar raíces reales y positivas
raices_positivas_analiticas = [r.evalf() for r in raices_analiticas if r.is_real and r > 0]
print(f"Raíces positivas de la solución analítica: {raices_positivas_analiticas}")

# Ejercicio 3.3: Aplicando el método de Heun
mostrar_ejercicio("3.3: Método de Heun")

h = 0.1
x_inicial, x_final = 0, 2
valor_inicial_y = 0

def edo(x, y):
    return -y + 10 * np.sin(3 * x)

x_puntos = np.arange(x_inicial, x_final + h, h)

# Aplicar el método de Heun
y_aproximados_heun = metodo_heun(edo, x_puntos, valor_inicial_y, h)

# Imprimir valores aproximados
for x_val, y_val in zip(x_puntos, y_aproximados_heun):
    print(f"x = {x_val:.1f}, y ≈ {y_val:.5f}")

# Graficar resultados de Heun
plt.plot(x_puntos, y_aproximados_heun, label='Método de Heun', marker='o', color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Método de Heun para la EDO')
plt.grid(True)
plt.legend()
plt.show()

# Ejercicio 3.4: Polinomio interpolante cúbico
mostrar_ejercicio("3.4: Polinomio interpolante")

polinomio_cubico = interp1d(x_puntos, y_aproximados_heun, kind='cubic')

# Graficar polinomio interpolante
x_interpolados = np.linspace(x_inicial, x_final, 100)
y_interpolados = polinomio_cubico(x_interpolados)

plt.plot(x_interpolados, y_interpolados, label='Interpolación cúbica', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación cúbica de Heun')
plt.grid(True)
plt.legend()
plt.show()

# Ajuste polinómico de grado 3
coeficientes = np.polyfit(x_puntos, y_aproximados_heun, 3)
polinomio_grado_3 = f"y = {coeficientes[0]:.5f}x^3 + {coeficientes[1]:.5f}x^2 + {coeficientes[2]:.5f}x + {coeficientes[3]:.5f}"
print(f"Polinomio ajustado: {polinomio_grado_3}")

# Ejercicio 3.5: Raíces del polinomio interpolante
mostrar_ejercicio("3.5: Raíces del polinomio interpolante")

raices = np.roots(coeficientes)
raices_positivas = [r for r in raices if r > 0]
print(f"Raíces positivas: {raices_positivas}")

# Ejercicio 3.6: Comparación de resultados (analítica, Heun, polinomio interpolante)
mostrar_ejercicio("3.6: Comparación de soluciones")

# Comparar solución analítica, método de Heun y polinomio interpolante
valores_analiticos = funcion_sol(x_puntos)
valores_interpolados = polinomio_cubico(x_puntos)
diferencias_heun = np.abs(np.array(valores_analiticos) - np.array(y_aproximados_heun))
diferencias_interp = np.abs(np.array(valores_analiticos) - np.array(valores_interpolados))

# Mostrar diferencias
print(f"{'x':>5} {'Analítica':>15} {'Heun':>15} {'Polinomio':>15} {'Dif Heun':>15} {'Dif Polinomio':>15}")
for x_val, analitica, heun, interp, dif_heun, dif_interp in zip(x_puntos, valores_analiticos, y_aproximados_heun, valores_interpolados, diferencias_heun, diferencias_interp):
    print(f"{x_val:>5.1f} {analitica:>15.5f} {heun:>15.5f} {interp:>15.5f} {dif_heun:>15.5f} {dif_interp:>15.5f}")

# Graficar comparaciones
plt.plot(x_puntos, valores_analiticos, label='Solución analítica', color='blue')
plt.plot(x_puntos, y_aproximados_heun, label='Método de Heun', marker='o', color='orange')
plt.plot(x_puntos, valores_interpolados, label='Polinomio interpolante (cúbico)', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparación entre Solución Analítica, Método de Heun y Polinomio Interpolante')
plt.grid(True)
plt.legend()
plt.show()

