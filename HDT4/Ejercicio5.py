import numpy as np

# Paso 1: Definir los puntos dados
x = np.array([-2, -1, 0, 1, 2, 3])
f_x = np.array([1, 4, 11, 16, 13, -4])

# Tabla de diferencias divididas
def diferencias_divididas(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y # Primera columna es f(x)

    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    return coef

# Calcular las diferencias divididas
coef = diferencias_divididas(x, f_x)

# Mostrar la tabla de diferencias divididas con nombres de las columnas
print("Tabla de diferencias divididas:")
print("Columna 1: f(x)")
print("Columna 2: Diferencias divididas de primer orden")
print("Columna 3: Diferencias divididas de segundo orden")
print("Columna 4: Diferencias divididas de tercer orden")
print("Columna 5 y siguientes: Diferencias divididas de orden superior")
print(coef)

# Paso 2: Construcción del polinomio usando el método de Newton
def polinomio_newton(coef, x_data, x):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n-k] + (x - x_data[n-k]) * p
    return p

# Crear el polinomio
def polinomio(x_value):
    return polinomio_newton(coef[0,:], x, x_value)

# Paso 3: Evaluar el polinomio y verificar si es de grado 3
print("\nPolinomio evaluado en los puntos x dados:")
for xi in x:
    print(f"P({xi}) = {polinomio(xi)}")

# Verificar si los valores coinciden con f(x)
if np.allclose([polinomio(xi) for xi in x], f_x):
    print("\nEl polinomio que interpola los datos es de grado 3.")
else:
    print("\nEl polinomio no es de grado 3.")
