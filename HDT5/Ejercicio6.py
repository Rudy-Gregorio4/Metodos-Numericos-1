import numpy as np

# Definir la función f(x, y) para la ecuación diferencial dada
def f(x, y):
    return 1 + x**2 * y**2

# Método de Runge-Kutta de 4to orden (RK4)
def runge_kutta_4(f, x0, y0, x_final, h):
    n = int((x_final - x0) / h) + 1
    x_vals = [x0]  # Inicializamos el primer valor de x
    y_vals = [y0]  # Inicializamos el primer valor de y

    x_n = x0
    y_n = y0

    for i in range(n - 1):
        k1 = h * f(x_n, y_n)
        k2 = h * f(x_n + h/2, y_n + k1/2)
        k3 = h * f(x_n + h/2, y_n + k2/2)
        k4 = h * f(x_n + h, y_n + k3)

        y_n = y_n + (k1 + 2*k2 + 2*k3 + k4) / 6
        y_n = round(y_n, 5)  # Redondeo a 5 cifras decimales
        x_n = round(x_n + h, 5)  # Redondeo a 5 cifras decimales para los valores de x

        x_vals.append(x_n)
        y_vals.append(y_n)

    return np.array(x_vals), np.array(y_vals)

# Función que representa la solución exacta (si se conoce)
# Para fines de ilustración, voy a asumir que tienes una función exacta,
# aquí coloco un placeholder que debe ser reemplazado por la verdadera solución exacta.
def solucion_exacta(x):
    # Reemplazar con la verdadera solución exacta si está disponible.
    # Esto es solo una suposición genérica para ilustrar el cálculo del error.
    return np.exp(x)  # Esto es solo un ejemplo

# Valores iniciales y de paso
x0 = 0
y0 = 1
x_final = 0.5
h = 0.1  # Tamaño de paso

# Obtener la aproximación de Runge-Kutta 4
x_vals_rk4, y_vals_rk4 = runge_kutta_4(f, x0, y0, x_final, h)

# Obtener la solución exacta para los valores de x
y_vals_exacta = solucion_exacta(x_vals_rk4)

# Calcular el error absoluto en cada punto
errores = np.abs(y_vals_exacta - y_vals_rk4)

# Mostrar los resultados con formato de tabla ajustado
print("\n" + "="*80)
print(f"{'Solución aproximada con el método de Runge-Kutta 4 (h = {h})':^80}")
print("-"*80)
print(f"{'x':^10} | {'y_aprox':^15} | {'y_exacta':^15} | {'Error':^15}")
print("-"*80)

for x, y_aprox, y_exac, error in zip(x_vals_rk4, y_vals_rk4, y_vals_exacta, errores):
    print(f"{x:^10.5f} | {y_aprox:^15.5f} | {y_exac:^15.5f} | {error:^15.5f}")

print("="*80)
