import numpy as np

class MedicationCalculator:
    def __init__(self, max_concentration_safe):
        self.max_concentration_safe = max_concentration_safe

    def calculate_concentration(self, A, t):
        return A * t * np.exp(-t / 3)

    def find_optimal_parameter(self):
        t_max = 3
        A = self.max_concentration_safe / (t_max * np.exp(-t_max / 3))
        return A

    def calculate_max_concentration(self, A):
        t_max = 3
        return self.calculate_concentration(A, t_max)

    def print_results(self, A, concentration_max):
        print(f"Cantidad de medicamento: {A:.5f} unidades")
        print(f"Concentración máxima: {concentration_max:.5f} mg/mL")
        print(f"Tiempo máxima de la concentración: {3} horas")

def main():
    calculator = MedicationCalculator(max_concentration_safe=1.0)
    A = calculator.find_optimal_parameter()
    concentration_max = calculator.calculate_max_concentration(A)
    calculator.print_results(A, concentration_max)

if __name__ == "__main__":
    main()