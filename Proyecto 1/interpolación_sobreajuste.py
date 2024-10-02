import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Cargar datos desde el archivo CSV con el delimitador adecuado
df = pd.read_csv(r'C:\Users\Rudy Gregorio\OneDrive\Desktop\Tareas\Semestre 6\Método Númericos\Proyecto 1\situacion_financiera.csv', delimiter=',')

# Verificar si la columna "Concepto" está presente en el archivo CSV
if 'Concepto' not in df.columns:
    print("Error: No se encontró la columna 'Concepto' en el archivo CSV.")
else:
    # Mostrar los conceptos disponibles al usuario
    conceptos_disponibles = df['Concepto'].unique()
    print("Conceptos disponibles:")
    for concepto in conceptos_disponibles:
        print(f"- {concepto}")

    # Solicitar al usuario que ingrese un concepto
    concepto_elegido = input("Por favor, ingresa el concepto que deseas consultar: ")

    # Verificar si el concepto ingresado existe en el CSV
    if concepto_elegido not in conceptos_disponibles:
        print(f"Error: El concepto '{concepto_elegido}' no está disponible en el archivo CSV.")
    else:
        # Filtrar los datos para el concepto seleccionado
        df_concepto = df[df['Concepto'] == concepto_elegido]

        # Convertir los valores de ingreso a tipo numérico (sin comas) y excluir el año 2020 si ya está presente
        years = np.array(df.columns[1:], dtype=int)
        income = df_concepto.iloc[0, 1:].replace(',', '', regex=True).astype(float).values

        # Revisar si el año 2020 ya está presente y excluirlo
        if 2020 in years:
            year_2020_index = np.where(years == 2020)
            years_excl_2020 = np.delete(years, year_2020_index)
            income_excl_2020 = np.delete(income, year_2020_index)
        else:
            years_excl_2020 = years
            income_excl_2020 = income

        # Verificar si los datos son constantes (para evitar errores de interpolación)
        if np.all(income_excl_2020 == income_excl_2020[0]):
            print(f"Los datos para el concepto '{concepto_elegido}' son constantes, no se puede realizar la interpolación.")
        else:
            # Interpolación lineal
            linear_interpolation_function = interp1d(years_excl_2020, income_excl_2020, kind='linear')

            # Calcular el nuevo valor para 2020 utilizando la interpolación lineal
            new_value_2020 = linear_interpolation_function(2020)

            # Agregar el nuevo valor interpolado a los datos para la gráfica
            years_with_new_2020 = np.append(years_excl_2020, 2020)
            income_with_new_2020 = np.append(income_excl_2020, new_value_2020)

            # Graficar
            plt.figure(figsize=(10, 6))
            plt.plot(years_excl_2020, income_excl_2020, 'o', label='Datos Originales sin 2020')
            plt.plot(2020, new_value_2020, 'ro', label=f'Nuevo Valor Interpolado para 2020: {new_value_2020:.2f}')
            plt.plot(np.sort(years_with_new_2020), np.sort(income_with_new_2020), '--', label='Interpolación Lineal (con 2020)')
            plt.title(f'Interpolación Lineal para {concepto_elegido} (Nuevo Valor en 2020)')
            plt.xlabel('Año')
            plt.ylabel('Millones de Quetzales')
            plt.legend()
            plt.grid(True)
            plt.show()
