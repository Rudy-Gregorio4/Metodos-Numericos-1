import numpy as np

def f(x):
    return (x + np.sqrt(x)) * (20 - x + np.sqrt(20 - x)) - 155.55

def f_prime(x):
    term1 = (1 + 1/(2 * np.sqrt(x))) * (20 - x + np.sqrt(20 - x))
    term2 = (x + np.sqrt(x)) * (-1 + 1/(2 * np.sqrt(20 - x)))
    return term1 + term2

def newton_raphson(x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fpx) < tol:
            return np.nan, i  # Regresa NaN (Not a Number) si la derivada es cercana a cero
        x_new = x - fx / fpx
        if i < 3:  # Imprimir las primeras 3 iteraciones
            print(f"Iteración {i+1}: x = {x:.4f}, fx = {fx:.4f}, fpx = {fpx:.4f}")
        if abs(x_new - x) < tol:
            print(f"Iteración {i+1}: x = {x_new:.4f}, fx = {fx:.4f}, fpx = {fpx:.4f}")  # Imprimir la última iteración
            return x_new, i + 1  # Regresa el resultado y la cantidad de iteraciones
        x = x_new
    print(f"Iteración {max_iter}: x = {x:.4f}, fx = {fx:.4f}, fpx = {fpx:.4f}")  # Imprimir la última iteración
    return np.nan, max_iter  # Regresa NaN si no se encontró una solución en el número máximo de iteraciones

# Punto inicial
x0 = 10

# Resolver la ecuación
x, iteraciones = newton_raphson(x0)

# Calcular y
y = 20 - x

# Imprimir los resultados
if np.isnan(x):
    print("No se encontró una solución.")
else:
    print(f"x = {x:.4f}")
    print(f"y = {y:.4f}")
    print(f"Iteraciones: {iteraciones}")