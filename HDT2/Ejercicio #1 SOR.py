import numpy as np

# Definir la matriz A y el vector b
A = np.array([
    [-1, 0, 0, np.sqrt(2)/2, 1, 0, 0, 0],
    [0, -1, 0, np.sqrt(2)/2, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 1/2, 0],
    [0, 0, 0, -np.sqrt(2)/2, 0, -1, -1/2, 0],
    [0, 0, 0, 0, -1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, -np.sqrt(2)/2, 0, 0, np.sqrt(3)/2, 0],
    [0, 0, 0, 0, 0, 0, -np.sqrt(3)/2, -1]
], dtype=float)

b = np.array([0, 0, 0, 0, 0, 10000, 0, 0], dtype=float)

# Método de SOR
def sor(A, b, omega=1.1, tol=1e-3, max_iterations=1000):
    n = len(b)
    x = np.zeros_like(b)
    iterations = 0
    
    # Almacenar los resultados de cada iteración
    history = []
    
    for _ in range(max_iterations):
        x_old = np.copy(x)
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            if A[i, i] == 0:
                raise ValueError(f"Element on diagonal at index {i} is zero.")
            x[i] = (1 - omega) * x_old[i] + omega * (b[i] - sum1 - sum2) / A[i, i]
        
        # Almacenar el estado de x en la historia
        history.append(np.copy(x))
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, iterations, history
        iterations += 1
        
    return x, iterations, history

# Resolver el sistema usando el método de SOR
try:
    sol_sor, num_iterations, history = sor(A, b, omega=1.1)
    sol_sor_rounded = np.round(sol_sor, 3)  # Redondear a 3 decimales
    
    # Mostrar las primeras tres iteraciones
    print("Primera, segunda y tercera iteración:")
    for i in range(min(3, len(history))):
        print(f"Iteración {i+1}: {np.round(history[i], 3)}")
    
    # Mostrar la solución final y el número total de iteraciones
    print("\nSolución final usando el método de SOR:")
    for value in sol_sor_rounded:
        print(value)
    print(f"Número total de iteraciones: {num_iterations}")
    
except ValueError as e:
    print(e)
