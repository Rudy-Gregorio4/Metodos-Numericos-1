import numpy as np
import matplotlib.pyplot as plt

# Parámetros iniciales
V_pulso = 5  # Voltaje del pulso (V)
t_pulso = 1e-3  # Duración del pulso (s)
t_max = 5e-3  # Tiempo máximo de simulación (s)
dt = 1e-6  # Paso de tiempo para RK4 (s)
L_min = 1e-6  # Inductancia mínima (H)
C_min = 1e-9  # Capacitancia mínima (F)

# Función de entrada: Pulso
def v_pulso(t):
    return V_pulso if 0 <= t <= t_pulso else 0

# Sistema de ecuaciones diferenciales para el circuito RLC
def sistema(t, x, R, L, C):
    x1, x2 = x
    dx1dt = x2
    dx2dt = (1 / L) * (v_pulso(t) - R * x2 - (x1 / C))
    return np.array([dx1dt, dx2dt])

# Método RK4
def rk4_step(f, t, x, h, R, L, C):
    k1 = f(t, x, R, L, C)
    k2 = f(t + h / 2, x + h * k1 / 2, R, L, C)
    k3 = f(t + h / 2, x + h * k2 / 2, R, L, C)
    k4 = f(t + h, x + h * k3, R, L, C)
    return x + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

# Simulación del circuito
def simular_circuito(R, L, C):
    t_vals = np.arange(0, t_max, dt)
    x_vals = np.zeros((len(t_vals), 2))  # [i(t), di/dt]
    x_vals[0] = [0, 0]  # Condiciones iniciales

    for i in range(1, len(t_vals)):
        t = t_vals[i - 1]
        x = x_vals[i - 1]
        x_vals[i] = rk4_step(sistema, t, x, dt, R, L, C)

    return t_vals, x_vals[:, 0]  # Retorna tiempo y corriente

# Análisis del comportamiento
def analizar_comportamiento(R, L, C):
    _, i_vals = simular_circuito(R, L, C)
    max_osc = np.max(np.abs(i_vals))
    overshoot = (max_osc / i_vals[-1]) - 1 if i_vals[-1] != 0 else np.inf

    if overshoot > 0.05:  # Subamortiguado: Oscilaciones significativas
        return "Subamortiguado"
    elif np.isclose(overshoot, 0, atol=0.01):  # Crítico: Sin oscilaciones y respuesta rápida
        return "Criticamente amortiguado"
    else:  # Sobreamortiguado: Sin oscilaciones y respuesta lenta
        return "Sobreamortiguado"

# Búsqueda de valores mínimos
def encontrar_valores_minimos():
    resultados = {}

    for L in np.linspace(L_min, 1e-3, 100):
        for C in np.linspace(C_min, 1e-6, 100):
            R_critico = 2 * np.sqrt(L / C)

            # Subamortiguado
            R = R_critico * 0.8
            if analizar_comportamiento(R, L, C) == "Subamortiguado":
                resultados['Subamortiguado'] = {'R': R, 'L': L, 'C': C}
                break

            # Crítico
            R = R_critico
            if analizar_comportamiento(R, L, C) == "Criticamente amortiguado":
                resultados['Criticamente amortiguado'] = {'R': R, 'L': L, 'C': C}
                break

            # Sobreamortiguado
            R = R_critico * 1.2
            if analizar_comportamiento(R, L, C) == "Sobreamortiguado":
                resultados['Sobreamortiguado'] = {'R': R, 'L': L, 'C': C}
                break

        if len(resultados) == 3:
            break

    return resultados

# Calcular y mostrar resultados
resultados = encontrar_valores_minimos()
for caso, valores in resultados.items():
    print(f"{caso}:")
    print(f"  Resistencia (R): {valores['R']:.4f} Ohms")
    print(f"  Inductancia (L): {valores['L']:.6e} H")
    print(f"  Capacitancia (C): {valores['C']:.6e} F\n")
