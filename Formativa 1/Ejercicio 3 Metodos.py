import numpy as np

def funcion(x):
    return np.tanh(x)

def metodo_secante(x0, x1, tol=1e-7, max_iter=100):
    for i in range(max_iter):
        if funcion(x1) == funcion(x0):
            return None, None  # Regresa None en caso de división por cero
        x2 = x1 - funcion(x1) * (x1 - x0) / (funcion(x1) - funcion(x0))
        
        if i < 3:  # Imprimir las primeras 3 iteraciones
            print(f"Iteración {i+1}: x0 = {x0:.4f}, x1 = {x1:.4f}, x2 = {x2:.4f}")
        
        if abs(x2 - x1) < tol:
            print(f"Iteración {i+1}: x0 = {x0:.4f}, x1 = {x1:.4f}, x2 = {x2:.4f}")  # Imprimir la última iteración
            return x2, i + 1  # Regresa el resultado y la cantidad de iteraciones
        
        x0, x1 = x1, x2
    
    print(f"Iteración {max_iter}: x0 = {x0:.4f}, x1 = {x1:.4f}, x2 = {x2:.4f}")  # Imprimir la última iteración
    return None, max_iter  # Regresa None en caso de no convergencia y la cantidad de iteraciones máximas

# Puntos iniciales
puntos_iniciales = [
    (1.08, 1.09),
    (1.09, 1.1),
    (1, 2.3),
    (1, 2.4)
]

# Aplicar el método de la secante a cada par de puntos iniciales
for x0, x1 in puntos_iniciales:
    print(f"Puntos iniciales: x0 = {x0}, x1 = {x1}")
    resultado, iteraciones = metodo_secante(x0, x1)
    if resultado is None:
        print("No convergencia o división por cero")
    else:
        print(f"Convergió: x = {resultado}, Iteraciones: {iteraciones}")