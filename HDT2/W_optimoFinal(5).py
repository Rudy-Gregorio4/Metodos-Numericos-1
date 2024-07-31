import numpy as np

def calcular_radio_espectral(A):
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    T_GS = np.dot(np.linalg.inv(D + L), -U)
    return max(abs(np.linalg.eigvals(T_GS)))

def calcular_omega_optimo(A):
    rho = calcular_radio_espectral(A)
    return 2 / (1 + np.sqrt(1 - rho**2))

def sor_method(A, b, X0, omega, tolerance=1e-3, max_iterations=100):
    n = len(b)
    X = X0.copy()
    for k in range(max_iterations):
        X_new = X.copy()
        for i in range(n):
            s1 = sum(A[i][j] * X_new[j] for j in range(i))
            s2 = sum(A[i][j] * X[j] for j in range(i + 1, n))
            X_new[i] = (1 - omega) * X[i] + (omega * (b[i] - s1 - s2)) / A[i][i]
        if np.linalg.norm(X_new - X, ord=np.inf) < tolerance:
            return X_new, k + 1
        X = X_new
    return X, max_iterations

# Definimos las matrices de coeficientes y los vectores de términos independientes
A_2_2 = np.array([
    [4, 1, -1, 1],
    [1, 4, -1, -1],
    [-1, -1, 5, 1],
    [1, -1, 1, 3]
])
b_2_2 = np.array([-2, -1, 0, 1])

A_2_3 = np.array([
    [4, -1, 0, 0, 0, 0],
    [-1, 4, -1, 0, 0, 0],
    [0, -1, 4, 0, 0, 0],
    [0, 0, 0, 4, -1, 0],
    [0, 0, 0, -1, 4, -1],
    [0, 0, 0, 0, -1, 4]
])
b_2_3 = np.array([0, 5, 0, 6, -2, 6])

# Calculamos los valores óptimos de omega
omega_opt_2_2 = calcular_omega_optimo(A_2_2)
omega_opt_2_3 = calcular_omega_optimo(A_2_3)

print(f"\nOmega óptimo para el sistema 2.2: {omega_opt_2_2:.4f}")
print(f"Omega óptimo para el sistema 2.3: {omega_opt_2_3:.4f}")

# Definimos el vector inicial
X0_2_2 = np.zeros(len(b_2_2))
X0_2_3 = np.zeros(len(b_2_3))

# Resolución de los sistemas con el omega óptimo
solution_2_2, iterations_2_2 = sor_method(A_2_2, b_2_2, X0_2_2, omega_opt_2_2)
solution_2_3, iterations_2_3 = sor_method(A_2_3, b_2_3, X0_2_3, omega_opt_2_3)

print("\nResultados:")
print("Sistema 2.2:")
print(f"  Solución: {solution_2_2}")
print(f"  Número de iteraciones: {iterations_2_2}")

print("\nSistema 2.3:")
print(f"  Solución: {solution_2_3}")
print(f"  Número de iteraciones: {iterations_2_3}")

# Formatear las salidas para que sean más legibles
def print_solution(system_label, solution, iterations):
    print(f"\nSistema {system_label}:")
    for i, x in enumerate(solution):
        print(f"  x{i + 1} = {x:.6f}")
    print(f"  Número de iteraciones: {iterations}")

print_solution("2.2", solution_2_2, iterations_2_2)
print_solution("2.3", solution_2_3, iterations_2_3)
