import numpy as np
import matplotlib.pyplot as plt

# Definimos la fuente de entrada como un pulso
def fuente_pulso(t, duracion=1e-3, amplitud=5):
    return amplitud if t <= duracion else 0

# Método de Euler para resolver el sistema
def metodo_euler(h, t_max, R, L, C):
    # Tiempo discretizado
    t = np.arange(0, t_max, h)
    n = len(t)
    
    # Variables iniciales
    x = np.zeros(n)  # Corriente (x)
    v = np.zeros(n)  # Derivada de la corriente (v)
    
    # Iteración de Euler
    for i in range(1, n):
        vin = fuente_pulso(t[i])
        dx_dt = v[i-1]
        dv_dt = (vin - R * v[i-1] - x[i-1] / C) / L
        x[i] = x[i-1] + h * dx_dt
        v[i] = v[i-1] + h * dv_dt
    
    return t, x, v

# Configuración para encontrar valores para cada caso
def calcular_valores(t_max=5e-3, h=1e-6):
    # Subamortiguado (ζ < 1)
    C = 1e-6  # Capacitancia fija
    L = 1e-3  # Inductancia fija
    R_critico = 2 * np.sqrt(L / C)
    R_sub = 0.8 * R_critico
    
    # Criticamente amortiguado (ζ = 1)
    R_crit = R_critico
    
    # Sobreamortiguado (ζ > 1)
    R_sob = 1.2 * R_critico
    
    # Simulaciones para cada caso
    resultados = {}
    for caso, R in zip(["Subamortiguado", "Criticamente amortiguado", "Sobreamortiguado"], 
                       [R_sub, R_crit, R_sob]):
        t, x, v = metodo_euler(h, t_max, R, L, C)
        resultados[caso] = {"R": R, "L": L, "C": C, "t": t, "x": x}
    
    return resultados

# Ejecutar simulaciones y mostrar resultados
resultados = calcular_valores()

# Graficar los resultados
plt.figure(figsize=(10, 6))
for caso, data in resultados.items():
    plt.plot(data["t"] * 1e3, data["x"], label=f"{caso} (R={data['R']:.2f} Ω)")
    
plt.title("Respuesta del circuito RLC - Método de Euler")
plt.xlabel("Tiempo (ms)")
plt.ylabel("Corriente (A)")
plt.legend()
plt.grid()
plt.show()

# Mostrar resultados numéricos
for caso, valores in resultados.items():
    print(f"{caso}:")
    print(f"  Resistencia (R): {valores['R']:.2f} Ω")
    print(f"  Inductancia (L): {valores['L']:.2e} H")
    print(f"  Capacitancia (C): {valores['C']:.2e} F\n")
