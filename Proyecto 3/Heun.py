import numpy as np
import matplotlib.pyplot as plt

# Fuente de pulso: un único pulso que va de 0 a 5V
def fuente_pulso(t, duracion=1e-3, amplitud=5):
    return amplitud if t <= duracion else 0

# Método de Heun para resolver el sistema
def metodo_heun(h, t_max, R, L, C):
    t = np.arange(0, t_max, h)  # Tiempo discretizado
    n = len(t)
    
    # Variables iniciales
    x = np.zeros(n)  # Corriente (x)
    v = np.zeros(n)  # Derivada de la corriente (v)
    
    for i in range(1, n):
        vin = fuente_pulso(t[i])
        
        # Pendiente inicial (en t_n)
        dx_dt = v[i-1]
        dv_dt = (vin - R * v[i-1] - x[i-1] / C) / L
        
        # Aproximación de Euler para t_{n+1}
        x_euler = x[i-1] + h * dx_dt
        v_euler = v[i-1] + h * dv_dt
        
        # Pendiente en t_{n+1} (Euler)
        dx_dt_euler = v_euler
        dv_dt_euler = (vin - R * v_euler - x_euler / C) / L
        
        # Actualización con Heun
        x[i] = x[i-1] + (h / 2) * (dx_dt + dx_dt_euler)
        v[i] = v[i-1] + (h / 2) * (dv_dt + dv_dt_euler)
    
    return t, x, v

# Configuración para encontrar valores para cada caso
def calcular_valores(h=1e-6, t_max=5e-3):
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
        t, x, v = metodo_heun(h, t_max, R, L, C)
        resultados[caso] = {"R": R, "L": L, "C": C, "t": t, "x": x}
    
    return resultados

# Ejecutar simulaciones y mostrar resultados
resultados_heun = calcular_valores()

# Graficar los resultados
plt.figure(figsize=(12, 8))

for caso, data in resultados_heun.items():
    plt.plot(data["t"] * 1e3, data["x"], label=f"Heun - {caso}", linestyle="-")

plt.title("Simulación del circuito RLC con el método de Heun")
plt.xlabel("Tiempo (ms)")
plt.ylabel("Corriente (A)")
plt.legend()
plt.grid()
plt.show()

# Mostrar resultados numéricos
print("Resultados de los cálculos:")
for caso, valores in resultados_heun.items():
    print(f"{caso}:")
    print(f"  Resistencia (R): {valores['R']:.2f} Ω")
    print(f"  Inductancia (L): {valores['L']:.2e} H")
    print(f"  Capacitancia (C): {valores['C']:.2e} F\n")
