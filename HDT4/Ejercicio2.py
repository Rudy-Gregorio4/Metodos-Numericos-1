import numpy as np
from scipy.interpolate import lagrange

# Datos del problema
horas = np.array([6, 8, 10, 12, 14, 16, 18, 20])
temperaturas = np.array([7, 9, 12, 18, 21, 19, 15, 10])

# Realizar la interpolación de Lagrange
polinomio_lagrange = lagrange(horas, temperaturas)

# Convertir el polinomio a la forma polinómica para que sea más legible
polinomio_lagrange_poly1d = np.poly1d(polinomio_lagrange)

# Mostrar el polinomio interpolante
print("El polinomio interpolante de Lagrange es:")
print(polinomio_lagrange_poly1d)

# Estimar las temperaturas para las horas solicitadas
temperatura_7h = polinomio_lagrange_poly1d(7)
temperatura_9h = polinomio_lagrange_poly1d(9)
temperatura_12h30 = polinomio_lagrange_poly1d(12.5)
temperatura_18h10 = polinomio_lagrange_poly1d(18.1)

# Mostrar los resultados
print(f"\nTemperaturas estimadas:")
print(f"A las 7:00: {temperatura_7h:.2f}°C")
print(f"A las 9:00: {temperatura_9h:.2f}°C")
print(f"A las 12:30: {temperatura_12h30:.2f}°C")
print(f"A las 18:10: {temperatura_18h10:.2f}°C")
