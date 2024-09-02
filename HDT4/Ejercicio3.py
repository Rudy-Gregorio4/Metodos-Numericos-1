import numpy as np

# Datos originales
x = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
y = np.array([1.62, 1.0, 0.75, 0.62, 0.52, 0.46])

# Método de diferencias divididas de Newton
def diferencias_divididas(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    
    return coef[0]

# Calcular coeficientes
coeficientes = diferencias_divididas(x, y)

# Mostrar el polinomio de Newton
def mostrar_polinomio(coeficientes, x):
    n = len(coeficientes)
    terminos = []

    # Primer término es f[x0]
    terminos.append(f"{coeficientes[0]:.4f}")

    # Añadir términos sucesivos
    for i in range(1, n):
        termino = f"{coeficientes[i]:+.4f}"
        for j in range(i):
            termino += f"*(x-{x[j]})"
        terminos.append(termino)

    # Combinar los términos en un polinomio
    polinomio = " ".join(terminos)
    return polinomio

# Función de interpolación
def polinomio_newton(coeficientes, x, xi):
    n = len(coeficientes) - 1
    p = coeficientes[n]
    for k in range(1, n + 1):
        p = coeficientes[n - k] + (xi - x[n - k]) * p
    return p

# Mostrar el polinomio original
polinomio = mostrar_polinomio(coeficientes, x)
print("Polinomio de Newton (original):")
print(polinomio)

# Estimar el volumen para una presión de 1.75 (original)
presion_175 = 1.75
volumen_175 = polinomio_newton(coeficientes, x, presion_175)
print(f"\nVolumen estimado para presión de {presion_175} (original): {volumen_175:.4f}")

# Nuevos datos incluyendo el punto adicional (3.5, 0.42)
x_nuevo = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5])
y_nuevo = np.array([1.62, 1.0, 0.75, 0.62, 0.52, 0.46, 0.42])

# Calcular nuevos coeficientes con el punto adicional
coeficientes_nuevos = diferencias_divididas(x_nuevo, y_nuevo)

# Mostrar el nuevo polinomio
polinomio_nuevo = mostrar_polinomio(coeficientes_nuevos, x_nuevo)
print("\nPolinomio de Newton (con punto adicional):")
print(polinomio_nuevo)

# Estimar el volumen para una presión de 1.75 con los nuevos datos
volumen_175_nuevo = polinomio_newton(coeficientes_nuevos, x_nuevo, presion_175)
print(f"\nVolumen estimado para presión de {presion_175} (con punto adicional): {volumen_175_nuevo:.4f}")
