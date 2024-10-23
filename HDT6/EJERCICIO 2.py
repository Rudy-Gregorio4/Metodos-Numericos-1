import numpy as np

# Definimos la solución analítica
def solucion_analitica(t):
    return (1/6) * t**3 * np.exp(t) - t * np.exp(t) + 2 * np.exp(t) - t - 2

def euler_method_con_error(h, t_max):
    # Definimos los valores de t
    t_values = np.arange(0, t_max + h, h)

    # Condiciones iniciales
    y1 = [0]  # y1(0) = y(0) = 0
    y2 = [0]  # y2(0) = y'(0) = 0
    errores = []  # Lista para guardar los errores

    # Método de Euler
    for t in t_values[:-1]:
        # Valores actuales
        y1_n = y1[-1]
        y2_n = y2[-1]

        # Derivadas (usamos el sistema de ecuaciones)
        y1_deriv = y2_n
        y2_deriv = 2 * y2_n - y1_n + t * np.exp(t) - t

        # Actualizamos los valores usando Euler
        y1_new = y1_n + h * y1_deriv
        y2_new = y2_n + h * y2_deriv

        # Almacenamos los nuevos valores
        y1.append(y1_new)
        y2.append(y2_new)

    # Mostramos solo los primeros 5 valores, puntos suspensivos, y los últimos 5 valores
    print("t\t y(t)_Euler\t y(t)_Analítica\t Error")
    for i, (t, y_aprox) in enumerate(zip(t_values, y1)):
        if i < 5:  # Mostrar los primeros 5 valores
            y_analitica = solucion_analitica(t)
            error = abs(y_analitica - y_aprox)
            errores.append(error)
            print(f"{t:.2f}\t {y_aprox:.6f}\t {y_analitica:.6f}\t {error:.6f}")
        elif i == 5:  # Mostrar puntos suspensivos después del 5to valor
            print("...\t ...\t\t ...\t\t ...")
        elif i >= len(t_values) - 5:  # Mostrar los últimos 5 valores
            y_analitica = solucion_analitica(t)
            error = abs(y_analitica - y_aprox)
            errores.append(error)
            print(f"{t:.2f}\t {y_aprox:.6f}\t {y_analitica:.6f}\t {error:.6f}")
    
    # Solución final
    print(f"\nSolución aproximada final en t = {t_max}: y({t_max}) = {y1[-1]:.6f}")

# Parámetros actualizados con h = 0.01
h = 0.01  # Tamaño de paso
t_max = 1.0  # Valor máximo de t

# Llamada al método de Euler con error usando h = 0.01
euler_method_con_error(h, t_max)
