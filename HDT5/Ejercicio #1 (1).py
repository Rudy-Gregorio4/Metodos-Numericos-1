import numpy as np

# Método de Euler
def euler(f, y0, t0, tf, h):
    n_steps = int((tf - t0) / h) + 1
    t = np.linspace(t0, tf, n_steps)
    y = np.zeros(n_steps)
    y[0] = y0
    for i in range(1, n_steps):
        y[i] = y[i - 1] + h * f(t[i - 1], y[i - 1])
    return t, y

# Ejercicio 1.1: f(t, y)
def f1(t, y):
    return -(y + 1) * (y + 3)

# Ejercicio 1.1: Solución exacta (solo para ilustrar, esta no es la solución exacta real)
def exact1(t):
    return -2 / (t + 1)  # Supongamos que es la solución exacta

# Ejercicio 1.2: f(t, y)
def f2(t, y):
    return -5 * y + 5 * t ** 2 + 27

# Ejercicio 1.2: Solución exacta (no necesariamente exacta)
def exact2(t):
    return t**2 + 3  # Ejemplo de una posible solución exacta

# Ejercicio 1.3: f(t, y)
def f3(t, y):
    return (y ** 2) / (1 + t)

# Ejercicio 1.3: Solución exacta (no necesariamente exacta)
def exact3(t):
    return -1 / np.log(1 + t)  # Ejemplo de solución exacta

# Ejercicio 1.4: f(t, y)
def f4(t, y):
    return t * np.exp(3 * t) - 2 * y

# Ejercicio 1.4: Solución exacta (no necesariamente exacta)
def exact4(t):
    return np.exp(3 * t) - t**2  # Ejemplo de solución exacta

# Parámetros para cada ejercicio
params = [
    {'f': f1, 'exact': exact1, 'y0': -2, 't0': 0, 'tf': 2, 'h': 0.2, 'label': 'Ejercicio 1.1'},
    {'f': f2, 'exact': exact2, 'y0': 1/3, 't0': 0, 'tf': 1, 'h': 0.1, 'label': 'Ejercicio 1.2'},
    {'f': f3, 'exact': exact3, 'y0': -1/np.log(2), 't0': 1, 'tf': 2, 'h': 0.1, 'label': 'Ejercicio 1.3'},
    {'f': f4, 'exact': exact4, 'y0': 0, 't0': 0, 'tf': 1, 'h': 0.5, 'label': 'Ejercicio 1.4'},
]

# Resolver y mostrar los resultados
for param in params:
    t, y_aprox = euler(param['f'], param['y0'], param['t0'], param['tf'], param['h'])
    print(f"Resultados para {param['label']}:")
    print(f"{'t':<10}{'y_aprox':<15}{'y_exact':<15}{'error (%)':<10}")
    
    for i in range(len(t)):
        y_exact = param['exact'](t[i])  # Calcular valor exacto
        error = abs((y_exact - y_aprox[i]) / y_exact) * 100  # Calcular error porcentual
        print(f"{t[i]:<10.2f}{y_aprox[i]:<15.5f}{y_exact:<15.5f}{error:<10.2f}")
    
    print("\n")
