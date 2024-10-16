import numpy as np

# Definir la función f(x, y) de la ecuación diferencial
def f(x, y):
    return 4 * np.exp(0.8 * x) - 0.5 * y

# Método de Euler mejorado con impresión del procedimiento
def euler_mejorado_procedimiento(f, x0, y0, x_final, h):
    # Número de pasos
    n = int((x_final - x0) / h)
    
    # Inicializar listas de x e y
    x_vals = np.linspace(x0, x_final, n+1)
    y_vals = np.zeros(n+1)
    y_vals[0] = y0  # Condición inicial

    # Iterar usando Euler mejorado (Heun)
    for i in range(n):
        x_n = x_vals[i]
        y_n = y_vals[i]
        
        # Predicción
        y_pred = y_n + h * f(x_n, y_n)
        print(f"Paso {i+1}:")
        print(f"Predicción: y_pred = y_n + h * f(x_n, y_n) = {y_n} + {h} * {f(x_n, y_n)} = {y_pred}")
        
        # Corrección
        y_corr = y_n + (h / 2) * (f(x_n, y_n) + f(x_n + h, y_pred))
        print(f"Corrección: y_{i+1} = y_n + (h/2) * (f(x_n, y_n) + f(x_n + h, y_pred))")
        print(f"         = {y_n} + ({h}/2) * ({f(x_n, y_n)} + {f(x_n + h, y_pred)}) = {y_corr}")
        print("-" * 50)
        
        # Actualizar valor corregido
        y_vals[i+1] = y_corr
    
    return x_vals, y_vals

# Método de Runge-Kutta de 4to orden (RK4)
def runge_kutta_4(f, x0, y0, x_final, h):
    # Número de pasos
    n = int((x_final - x0) / h)
    
    # Inicializar listas de x e y
    x_vals = np.linspace(x0, x_final, n+1)
    y_vals = np.zeros(n+1)
    y_vals[0] = y0  # Condición inicial

    # Iterar usando RK4
    for i in range(n):
        x_n = x_vals[i]
        y_n = y_vals[i]
        
        k1 = h * f(x_n, y_n)
        k2 = h * f(x_n + h/2, y_n + k1/2)
        k3 = h * f(x_n + h/2, y_n + k2/2)
        k4 = h * f(x_n + h, y_n + k3)
        
        y_vals[i+1] = y_n + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return x_vals, y_vals

# Solución analítica de la ecuación diferencial
def solucion_analitica(x):
    return (2 * np.exp(-0.5 * x) + 4 * np.exp(0.8 * x))

# Valores iniciales
x0 = 0
y0 = 2
x_final = 4
h = 0.1  # Tamaño de paso

# Llamar al método de RK4
x_vals_rk4, y_vals_rk4 = runge_kutta_4(f, x0, y0, x_final, h)

# Calcular la solución analítica
x_vals_exacta = np.linspace(x0, x_final, len(x_vals_rk4))
y_vals_exacta = solucion_analitica(x_vals_exacta)

# Comparar con Euler mejorado
x_vals_euler, y_vals_euler = euler_mejorado_procedimiento(f, x0, y0, x_final, h)

# Mostrar resultados
print(f"Valor de y(4) con RK4: {y_vals_rk4[-1]}")
print(f"Valor de y(4) con Euler mejorado: {y_vals_euler[-1]}")
