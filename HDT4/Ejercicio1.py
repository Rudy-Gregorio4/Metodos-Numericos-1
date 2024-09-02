import numpy as np
from scipy.interpolate import lagrange
import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
years = np.array([1950, 1973, 1994, 2002])
population = np.array([2.79, 5.16, 8.33, 11.24])

# Inciso 1.2: Calcular el polinomio de Lagrange de grado 3
polynomial = lagrange(years, population)

# Mostrar el polinomio completo
print("El polinomio de Lagrange de grado 3 es:")
print(np.poly1d(polynomial))

# Coeficientes del polinomio (de mayor a menor grado)
coef = polynomial.coef
grados = [f"x^{i}" for i in range(len(coef)-1, -1, -1)]

# Crear un DataFrame para mostrar los coeficientes
df = pd.DataFrame({"Grado": grados, "Coeficiente": coef})

print("\nCoeficientes del polinomio por grado:")
print(df)

# Inciso 1.3: Validación de la regresión exponencial
# Usamos los mismos años y poblaciones
selected_years = years
selected_population = population

# Realizamos una regresión exponencial en los mismos puntos
log_population = np.log(selected_population)
coeffs = np.polyfit(selected_years, log_population, 1)

# Coeficientes de la regresión exponencial
A = np.exp(coeffs[1])
B = coeffs[0]

# Ajustar la visualización usando notación científica
print(f"\nCoeficientes de la regresión exponencial:")
print(f"A = {A:.4e}, B = {B:.4f}")

# Función de regresión exponencial
def exp_model(x, A, B):
    return A * np.exp(B * x)

# Extender el rango de años para ver la tendencia
extended_years = np.linspace(1950, 2050, 200)  # Extendemos hasta el año 2050
exp_values = exp_model(extended_years, A, B)

# Graficar la curva exponencial ajustada y los puntos originales
plt.figure(figsize=(10, 6))
plt.plot(extended_years, exp_values, label='Regresión Exponencial', color='green')
plt.scatter(selected_years, selected_population, color='red', label='Datos de Población')
plt.title('Regresión Exponencial vs Datos (extendida)')
plt.xlabel('Año')
plt.ylabel('Millones de personas')
plt.grid(True)
plt.legend()
plt.show()

# Inciso 1.4: Pronóstico de la población en 2024
year_to_predict = 2024
predicted_population_2024 = exp_model(year_to_predict, A, B)
print(f"\nLa población pronosticada de Guatemala para el año {year_to_predict} es: {predicted_population_2024:.2f} millones de personas.")
