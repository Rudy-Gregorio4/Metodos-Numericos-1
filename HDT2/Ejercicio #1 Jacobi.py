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

# Método de Jacobi
def jacobi(A, b, tol=1e-3, max_iterations=1000):
    n = len(b)
    x = np.zeros_like(b)
    D = np.diag(A)
    R = A - np.diagflat(D)
    iterations = 0
    
    # Almacenar los resultados de cada iteración
    history = []
    
    for _ in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            if A[i, i] == 0:
                raise ValueError(f"Element on diagonal at index {i} is zero.")
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        # Almacenar el estado de x_new en la historia
        history.append(np.copy(x_new))
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iterations, history
        x = x_new
        iterations += 1
        
    return x, iterations, history

# Resolver el sistema usando el método de Jacobi
try:
    sol_jacobi, num_iterations, history = jacobi(A, b)
    sol_jacobi_rounded = np.round(sol_jacobi, 3)  # Redondear a 3 decimales
    
    # Mostrar las primeras tres iteraciones
    print("Primera, segunda y tercera iteración:")
    for i in range(min(3, len(history))):
        print(f"Iteración {i+1}: {np.round(history[i], 3)}")
        
    # Mostrar la solución final y el número total de iteraciones
    print("\nSolución final usando el método de Jacobi:")
    for value in sol_jacobi_rounded:
        print(value)
    print(f"Número total de iteraciones: {num_iterations}")
        
except ValueError as e:
    print(e)
