import numpy as np

# Definir la función f(x, y) de la ecuación diferencial
def f(x, y):
    return x - y

# Método de Runge-Kutta de 4to orden (RK4) corregido para los incrementos exactos
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
        y_n = round(y_n, 5)
        x_n = round(x_n + h, 2)  # Aseguramos que x_n incremente exactamente en pasos de h

        x_vals.append(x_n)
        y_vals.append(y_n)

    return np.array(x_vals), np.array(y_vals)

# Solución exacta para la ecuación diferencial y' = x - y con y(1) = 2
def solucion_exacta(x):
    C = 3 * np.exp(-1) + 1  # Constante calculada con la condición inicial y(1) = 2
    return C * np.exp(-x) + x - 1

# Valores iniciales y de paso
x0 = 1
y0 = 2
x_final = 1.2
h = 0.02  # Tamaño de paso

# Obtener la aproximación de Runge-Kutta 4
x_vals_rk4, y_vals_rk4 = runge_kutta_4(f, x0, y0, x_final, h)

# Calcular la solución exacta para los mismos puntos
sol_exacta = solucion_exacta(x_vals_rk4)

# Calcular el error en cada punto
errores = np.abs(sol_exacta - y_vals_rk4)

# Mostrar los resultados con formato de tabla ajustado
print("\n" + "="*60)
print(f"{'Solución aproximada con el método de Runge-Kutta 4 (h = {0.02})':^60}")
print("-"*60)
print(f"{'x':^10} | {'y_aprox':^15} | {'y_exacta':^15} | {'Error (%)':^15}")
print("-"*60)

for x, y_aprox, y_exacta, error in zip(x_vals_rk4, y_vals_rk4, sol_exacta, errores):
    print(f"{x:^10.2f} | {y_aprox:^15.5f} | {y_exacta:^15.5f} | {error:^15.5f}")

print("="*60)
