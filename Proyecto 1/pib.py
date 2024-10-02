import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Función para cargar los datos desde un archivo CSV
def cargar_datos(file_path):
    # Lee el archivo CSV y elimina las columnas innecesarias
    df = pd.read_csv(file_path).drop(columns=["Unnamed: 22", "Unnamed: 23"])
    return df

# Función para realizar la regresión lineal y estimar valores futuros
def estimar_regresion(df, concepto):
    # Extrae los años (columnas) y los convierte a un array de enteros
    years = np.array([int(year) for year in df.columns[1:]])
    
    # Extrae los valores correspondientes al concepto elegido
    valores = df[df['Concepto'] == concepto].iloc[0, 1:].values.astype(float)

    # Crea un modelo de regresión lineal
    model = LinearRegression()
    
    # Reshape de los años para que sea una matriz columna (necesaria para la regresión)
    years_reshaped = years.reshape(-1, 1)
    
    # Ajusta el modelo de regresión lineal con los años y los valores
    model.fit(years_reshaped, valores)

    # Define los años futuros a predecir (2024 y 2025)
    future_years = np.array([2024, 2025]).reshape(-1, 1)
    
    # Realiza las predicciones para los años futuros
    predicciones = model.predict(future_years)
    
    # Devuelve los años, valores originales, años futuros, y las predicciones
    return years, valores, future_years, predicciones

# Función para mostrar el gráfico con los datos históricos y las predicciones
def mostrar_grafico(years, valores, future_years, predicciones, concepto):
    plt.figure(figsize=(10, 6))
    
    # Grafica los datos históricos con líneas continuas y círculos
    plt.plot(years, valores, 'o-', label=f'{concepto} (2003-2023)')
    
    # Grafica las predicciones con líneas discontinuas y círculos
    plt.plot(future_years, predicciones, 'o--', label=f'Estimación {concepto} (2024-2025)')
    
    # Configura las etiquetas de los ejes y el título
    plt.xlabel('Año')
    plt.ylabel('Millones de Quetzales')
    plt.title(f'Estimaciones de {concepto} para 2024 y 2025')
    
    # Muestra la leyenda y la cuadrícula
    plt.legend()
    plt.grid(True)
    
    # Muestra la gráfica en pantalla
    plt.show()

# Función principal del programa
def main():
    # Definir la ruta del archivo CSV
    file_path = r'C:\Users\Rudy Gregorio\OneDrive\Desktop\Tareas\Semestre 6\Método Númericos\Proyecto 1\pib.csv'
    
    # Cargar los datos desde el archivo CSV
    df = cargar_datos(file_path)

    # Mostrar al usuario los conceptos disponibles en el archivo
    print("Conceptos disponibles:")
    for concepto in df['Concepto']:
        print(f"- {concepto}")

    # Solicitar al usuario que ingrese el concepto que desea analizar
    concepto = input("\nIngrese el nombre del concepto que desea analizar exactamente como aparece: ")

    # Verificar si el concepto ingresado existe en el archivo
    if concepto in df['Concepto'].values:
        # Realizar la regresión lineal y obtener las estimaciones
        years, valores, future_years, predicciones = estimar_regresion(df, concepto)
        
        # Mostrar las estimaciones en la consola antes de la gráfica
        print(f"\nEstimaciones para {concepto} 2024: {predicciones[0]}")
        print(f"Estimaciones para {concepto} 2025: {predicciones[1]}\n")

        # Mostrar la gráfica con los datos y las predicciones
        mostrar_grafico(years, valores, future_years, predicciones, concepto)
    else:
        # Mostrar un mensaje de error si el concepto no se encuentra
        print("Concepto no encontrado. Por favor, verifique la ortografía y vuelva a intentarlo.")

# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
