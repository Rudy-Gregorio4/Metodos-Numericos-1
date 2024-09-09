import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos
x = np.array([3.0, 4.5, 7.0, 9.0])  # Valores de x
y = np.array([2.5, 1.0, 2.5, 0.5])  # Valores de y correspondientes

# Valor de x para el cual queremos estimar el valor de y
x_val = 5.0

# ---- Parte 1.2: Interpolación lineal ----
# Construimos el trazador lineal
trazador_lineal = interp1d(x, y, kind='linear')

# Estimamos el valor de y correspondiente a x = 5 usando el trazador lineal
y_linear = trazador_lineal(x_val)

# Mostrar el procedimiento y resultado en la terminal
print(f"1.2. Valor estimado de y en x = {x_val} con interpolación lineal: y = {y_linear}\n")

# ---- Parte 1.3: Oscilación de los polinomios interpolantes ----
print("\n1.3. ¿Los trazadores lineales resuelven el problema de oscilación?")
print("Respuesta: Sí, la interpolación lineal no presenta oscilaciones, ya que utiliza líneas rectas entre los puntos de datos.\n")

# ---- Parte 1.4: Interpolación cuadrática ----
# Construimos el trazador cuadrático
trazador_cuadratico = interp1d(x, y, kind='quadratic')

# Estimamos el valor de y correspondiente a x = 5 usando el trazador cuadrático
y_quad = trazador_cuadratico(x_val)

# Mostrar el procedimiento y resultado
print(f"1.4. Estimación con trazador cuadrático:")
print(f"Valor estimado de y en x = {x_val} con interpolación cuadrática: y = {y_quad}\n")

# Conclusión sobre oscilaciones en interpolación cuadrática
print("¿Oscila significativamente el polinomio cuadrático?")
print("Respuesta: No, el polinomio cuadrático sigue suavemente los datos sin mostrar oscilaciones significativas.\n")

# ---- Parte 1.5: Interpolación cúbica ----
# Construimos el trazador cúbico
trazador_cubico = interp1d(x, y, kind='cubic')

# Estimamos el valor de y correspondiente a x = 5 usando el trazador cúbico
y_cubic = trazador_cubico(x_val)

# Mostrar el procedimiento y resultado
print(f"1.5. Estimación con trazador cúbico:")
print(f"Valor estimado de y en x = {x_val} con interpolación cúbica: y = {y_cubic}\n")

# Gráfica de los puntos originales y las interpolaciones
x_plot = np.linspace(min(x), max(x), 500)
y_linear_plot = trazador_lineal(x_plot)
y_quad_plot = trazador_cuadratico(x_plot)
y_cubic_plot = trazador_cubico(x_plot)

plt.scatter(x, y, color='red', label='Datos Originales')
plt.plot(x_plot, y_linear_plot, label='Interpolación Lineal', linestyle='--', color='blue')
plt.plot(x_plot, y_quad_plot, label='Interpolación Cuadrática', linestyle='-', color='green')
plt.plot(x_plot, y_cubic_plot, label='Interpolación Cúbica', linestyle='-', color='orange')
plt.scatter(x_val, y_cubic, color='purple', label=f'Estimación cúbica en x={x_val}')
plt.title('Comparación de Interpolaciones')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Conclusión sobre oscilaciones cúbicas
print(f"¿Oscila significativamente el polinomio cúbico? No, el polinomio cúbico no presenta oscilaciones drásticas y sigue los datos suavemente.\n")
