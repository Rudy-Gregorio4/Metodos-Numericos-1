import math

# 1. Valores conocidos
x0 = 0       # Primer punto conocido
x1 = 0.5     # Segundo punto conocido
f_x0 = math.exp(x0)   # f(x0) = e^0 = 1
f_x1 = math.exp(x1)   # f(x1) ≈ e^0.5 ≈ 1.64872

# Mostrar valores iniciales
print(f"x0 = {x0}, f(x0) = {f_x0:.5f}")
print(f"x1 = {x1}, f(x1) = {f_x1:.5f}")

# 2. Punto de interpolación
x = 0.25    # Punto donde queremos aproximar f(x)

# Mostrar punto de interpolación
print(f"\nInterpolando para x = {x}")

# 3. Procedimiento de interpolación lineal
# Cálculo del numerador (f(x1) - f(x0))
numerador = f_x1 - f_x0
print(f"Numerador: f(x1) - f(x0) = {f_x1:.5f} - {f_x0:.5f} = {numerador:.5f}")

# Cálculo del denominador (x1 - x0)
denominador = x1 - x0
print(f"Denominador: x1 - x0 = {x1} - {x0} = {denominador:.2f}")

# Cálculo de la pendiente (numerador / denominador)
pendiente = numerador / denominador
print(f"Pendiente: {numerador:.5f} / {denominador:.2f} = {pendiente:.5f}")

# Cálculo de la interpolación f(x)
f_x = f_x0 + pendiente * (x - x0)
print(f"\nf({x}) ≈ f({x0}) + pendiente * (x - {x0})")
print(f"f({x}) ≈ {f_x0:.5f} + {pendiente:.5f} * ({x} - {x0})")
print(f"f({x}) ≈ {f_x:.5f}")
