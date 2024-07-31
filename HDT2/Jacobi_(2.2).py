import numpy as np

def jacobi_method(A, b, X0, tolerance=1e-3, max_iterations=100):
    """
    Resolución de un sistema de ecuaciones lineales usando el método de Jacobi.

    Parámetros:
    A (numpy.ndarray): Matriz de coeficientes.
    b (numpy.ndarray): Vector de términos independientes.
    X0 (numpy.ndarray): Vector inicial de solución.
    tolerance (float): Tolerancia para la convergencia.
    max_iterations (int): Número máximo de iteraciones.

    Retorna:
    numpy.ndarray: Vector solución.
    int: Número de iteraciones realizadas.
    """
    n = len(b)  # Número de ecuaciones
    X = X0.copy()  # Copiar el vector inicial para evitar modificar el original
    for k in range(max_iterations):  # Iterar hasta el número máximo de iteraciones
        X_new = np.zeros_like(X)  # Inicializar un nuevo vector de soluciones
        print(f"Iteración {k + 1}:")  # Imprimir el número de iteración
        for i in range(n):  # Iterar sobre cada ecuación
            s = sum(A[i][j] * X[j] for j in range(n) if j != i)  # Calcular la suma de A[i][j] * X[j] para j != i
            X_new[i] = (b[i] - s) / A[i][i]  # Actualizar el valor de X_new[i] según la fórmula de Jacobi
            print(f"  x{i+1} = {X_new[i]:.6f}")  # Imprimir el valor de la variable calculada
        
        # Verificar la convergencia usando la norma del supremo (norma infinito)
        if np.linalg.norm(X_new - X, ord=np.inf) < tolerance:
            print(f"Convergencia alcanzada después de {k + 1} iteraciones.")
            return X_new, k  # Si la solución converge, retornar la solución y el número de iteraciones
        
        X = X_new  # Actualizar X para la siguiente iteración
    print("Número máximo de iteraciones alcanzado sin convergencia.")
    return X, max_iterations  # Retornar la solución y el número máximo de iteraciones si no converge

# Ejemplo de uso
if __name__ == "__main__":
    # Definir la matriz de coeficientes A y el vector de términos independientes b del nuevo sistema de ecuaciones
    A = np.array([[ 4,  1, -1,  1],
                  [ 1,  4, -1, -1],
                  [-1, -1,  5,  1],
                  [ 1, -1,  1,  3]])
    b = np.array([-2, -1, 0, 1])

    # Vector inicial X0 (vector de ceros)
    X0 = np.zeros(len(b))

    # Tolerancia y número máximo de iteraciones
    tolerance = 1e-3
    max_iterations = 100

    # Resolver el sistema utilizando el método de Jacobi
    solution, iterations = jacobi_method(A, b, X0, tolerance, max_iterations)
    
    # Imprimir la solución y el número de iteraciones
    print("Solución final:", solution)
    print("Número de iteraciones:", iterations)
