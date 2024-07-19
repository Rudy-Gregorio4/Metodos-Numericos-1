import numpy as np
import matplotlib.pyplot as plt

# Definimos la función F(x)
def F(x):
    return 0.5 + 0.25 * x**2 - x * np.sin(x) - 0.5 * np.cos(2 * x)

# Definimos la derivada F'(x)
def F_prime(x):
    return 0.5 * x - np.sin(x) - x * np.cos(x) + np.sin(2 * x)

# Implementamos el método de Newton-Raphson con depuración
def newton_raphson(x0, tol=1e-6, max_iter=1000):
    x = x0
    iteraciones = []
    valores_x = []
    
    for i in range(max_iter):
        Fx = F(x)
        Fpx = F_prime(x)
        if Fpx == 0:
            raise ValueError("Derivada cero, no se puede continuar.")
        
        x_new = x - Fx / Fpx
        
        iteraciones.append(i + 1)
        valores_x.append(x_new)
        
        print(f"Iteración {i+1}: x = {x}, F(x) = {Fx}, F'(x) = {Fpx}, x_new = {x_new}")
        
        if abs(x_new - x) < tol:
            return x_new, i+1, iteraciones, valores_x
        
        x = x_new
    
    raise ValueError("No se encontró la raíz en el número máximo de iteraciones.")

# Valor inicial
x0 = np.pi*10

# Llamamos a la función de Newton-Raphson
try:
    root, iterations, iteraciones, valores_x = newton_raphson(x0)
    print(f"La raíz aproximada es: {root}")
    print(f"Número de iteraciones: {iterations}")
   
    
    # Graficamos la función F(x) y la raíz encontrada
    x = np.linspace(0, 2 * np.pi, 400)
    y = F(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='$F(x)$')
    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(root, color='red', linestyle='--', label=f'Raíz aproximada: {root:.6f}')
    plt.scatter(valores_x, F(np.array(valores_x)), color='red', zorder=5)
    
    plt.title('Método de Newton-Raphson')
    plt.xlabel('$x$')
    plt.ylabel('$F(x)$')
    plt.legend()
    plt.grid(True)
    plt.show()
    
except ValueError as e:
    print(e)
