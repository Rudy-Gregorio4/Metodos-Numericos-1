# Definir los puntos conocidos
x_values = [0.698, 0.733, 0.768, 0.803]
f_values = [0.7661, 0.7432, 0.7193, 0.6946]

# Punto a interpolar
x = 0.75

# Función para calcular L_i(x)
def lagrange_basis(x, i, x_values):
    L_i = 1
    for j in range(len(x_values)):
        if i != j:
            L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])
    return L_i

# Función para generar la expresión simbólica de L_i(x)
def lagrange_basis_expr(i, x_values):
    terms = []
    for j in range(len(x_values)):
        if i != j:
            terms.append(f"(x - {x_values[j]}) / ({x_values[i]} - {x_values[j]})")
    return " * ".join(terms)

# Calcular P(x) usando la interpolación de Lagrange
P_x = 0
lagrange_polynomial = []
for i in range(len(x_values)):
    L_i = lagrange_basis(x, i, x_values)
    term = f_values[i] * L_i
    P_x += term
    
    # Construir el polinomio de Lagrange
    L_i_expr = lagrange_basis_expr(i, x_values)
    lagrange_polynomial.append(f"{f_values[i]} * ({L_i_expr})")

    # Mostrar L_i(x) y su contribución
    print(f"L_{i}(x) = {L_i_expr}")
    print(f"Término {i}: {f_values[i]} * L_{i}(x) = {term}\n")

# Mostrar el polinomio de Lagrange completo
polynomial_str = " + \n".join(lagrange_polynomial)
print(f"El polinomio de Lagrange es:\nP(x) = {polynomial_str}")

# Mostrar el valor de la aproximación final
print(f"\nAproximación de f({x}) usando el polinomio de interpolación de Lagrange es: {P_x}")
