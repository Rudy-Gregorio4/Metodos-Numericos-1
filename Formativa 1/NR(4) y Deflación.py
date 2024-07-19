import numpy as np
import matplotlib.pyplot as plt

# Definimos la función del polinomio f(x)
def f(x):
    return x**4 + 5*x**3 - 9*x**2 - 85*x - 136

# Definimos la derivada del polinomio f'(x)
def f_prime(x):
    return 4*x**3 + 15*x**2 - 18*x - 85

# Implementamos el método de Newton-Raphson
def newton_raphson(x0, tol=1e-5, max_iter=1000):
    x = x0
    for i in range(max_iter):
        Fx = f(x)
        Fpx = f_prime(x)
        if Fpx == 0:
            raise ValueError("Derivada cero, no se puede continuar.")
        
        x_new = x - Fx / Fpx
        
        if abs(x_new - x) < tol:
            return x_new
        
        x = x_new
    
    raise ValueError("No se encontró la raíz en el número máximo de iteraciones.")

# Implementamos la deflación para reducir el grado del polinomio
def deflate_poly(coeffs, root):
    n = len(coeffs) - 1
    new_coeffs = [0] * n
    new_coeffs[0] = coeffs[0]
    for i in range(1, n):
        new_coeffs[i] = coeffs[i] + root * new_coeffs[i - 1]
    return new_coeffs

# Encontramos todas las raíces del polinomio utilizando NR y deflación
def find_all_roots(coeffs, initial_guesses, tol=1e-5):
    roots = []
    for x0 in initial_guesses:
        try:
            root = newton_raphson(x0, tol)
            roots.append(root)
            coeffs = deflate_poly(coeffs, root)
            deflated_poly = np.poly1d(coeffs)
            global f, f_prime
            f = deflated_poly
            f_prime = deflated_poly.deriv()
        except ValueError as e:
            print(e)
            continue
    return roots

# Coeficientes del polinomio f(x)
coeffs = [1, 5, -9, -85, -136]
polynomial = np.poly1d(coeffs)

# Funciones f(x) y f'(x) basadas en los coeficientes del polinomio
f = polynomial
f_prime = polynomial.deriv()

# Valores iniciales
initial_guesses = [1, -1, 2, -2]

# Encontramos todas las raíces
roots = find_all_roots(coeffs, initial_guesses)
print(f"Las raíces aproximadas del polinomio son: {roots}")

# Graficamos el polinomio y las raíces encontradas
x = np.linspace(-10, 10, 400)
y = polynomial(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='$f(x) = x^4 + 5x^3 - 9x^2 - 85x - 136$')
plt.axhline(0, color='gray', lw=0.5)
plt.scatter(roots, [0]*len(roots), color='red', zorder=5)

plt.title('Raíces del polinomio usando NR y deflación')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.grid(True)
plt.show()
