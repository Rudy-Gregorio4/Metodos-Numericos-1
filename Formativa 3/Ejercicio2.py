import numpy as np
import matplotlib.pyplot as plt

# Definir los nodos
x_nodes = np.linspace(0, 1, 4)  # 4 nodos
y_nodes = np.sin(2 * np.pi * x_nodes)  # valores de f(x) en los nodos

# Aproximación del trazador cuadrático manualmente
def quadratic_spline_equations(x_nodes, y_nodes):
    n = len(x_nodes) - 1  # número de intervalos
    coefs = []  # para almacenar los coeficientes de los polinomios cuadráticos
    
    # El primer polinomio será de la forma f(x) = a*(x - x0)^2 + b*(x - x0) + c
    # Para el primer intervalo [x0, x1]
    for i in range(n):
        x0 = x_nodes[i]
        x1 = x_nodes[i+1]
        y0 = y_nodes[i]
        y1 = y_nodes[i+1]

        # Calculamos los coeficientes a, b, c para el polinomio cuadrático en este intervalo
        # Polinomio de la forma f(x) = a(x - x0)^2 + b(x - x0) + c
        # Necesitamos garantizar continuidad en el punto de conexión
        a = (y1 - y0) / ((x1 - x0)**2)
        b = 0  # Para asegurar que no haya una pendiente extraña
        c = y0
        coefs.append((a, b, c))
        
        # Mostrar la ecuación en la terminal
        print(f"Para el intervalo [{x0}, {x1}]:")
        print(f"f(x) = {a:.4f}(x - {x0})^2 + {b:.4f}(x - {x0}) + {c:.4f}\n")
    
    return coefs

# Crear una función que evalúe el polinomio cuadrático adecuado para un valor x
def quadratic_spline(x, x_nodes, y_nodes, coefs):
    intervals = [(x_nodes[i], x_nodes[i+1]) for i in range(len(x_nodes)-1)]
    
    for i in range(len(intervals)):
        x0, x1 = intervals[i]
        if x0 <= x <= x1:
            a, b, c = coefs[i]
            return a*(x - x0)**2 + b*(x - x0) + c

# Calcular las ecuaciones de los trazadores cuadráticos
coefs = quadratic_spline_equations(x_nodes, y_nodes)

# Crear una lista de puntos para graficar la función
x_vals = np.linspace(0, 1, 100)
y_vals = [quadratic_spline(x, x_nodes, y_nodes, coefs) for x in x_vals]

# Graficar el resultado
plt.plot(x_vals, y_vals, label='Spline Cuadrático')
plt.scatter(x_nodes, y_nodes, color='red', label='Nodos')
plt.plot(x_vals, np.sin(2 * np.pi * x_vals), '--', label='f(x) = sin(2πx)', color='green')
plt.legend()
plt.title('Aproximación con Trazador Cuadrático')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
