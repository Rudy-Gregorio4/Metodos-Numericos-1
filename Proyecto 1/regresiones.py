import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Función para cargar los datos desde un archivo CSV con manejo de excepciones
def cargar_datos(file_path):
    try:
        # Cargar el archivo CSV en un DataFrame de pandas
        df = pd.read_csv(file_path)
        print(f"Datos cargados correctamente desde {file_path}.")
        return df
    except FileNotFoundError:
        print("Error: El archivo no se encuentra. Verifica la ruta.")
    except pd.errors.ParserError:
        print("Error: El archivo CSV está mal formateado.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None

# Función para realizar la regresión polinómica y estimar valores futuros
def estimar_regresion_polinomica(df, concepto, grado=2):
    # Extrae los años (columnas) y los convierte a un array de enteros
    years = np.array([int(year) for year in df.columns[1:]])
    print(f"Años extraídos del archivo CSV: {years}")

    # Extrae los valores correspondientes al concepto elegido, eliminando las comas y convirtiendo a float
    try:
        valores = df[df['Concepto'] == concepto].iloc[0, 1:].str.replace(',', '').astype(float).values
        print(f"Valores correspondientes al concepto '{concepto}' extraídos: {valores}")
    except Exception as e:
        print(f"Error procesando los datos: {e}")
        return None, None, None, None

    # Crea un modelo de regresión polinómica
    print(f"Creando modelo de regresión polinómica de grado {grado}.")
    polynomial_features = PolynomialFeatures(degree=grado)

    # Reshape de los años para que sea una matriz columna (necesaria para la regresión)
    years_reshaped = years.reshape(-1, 1)
    print(f"Años reformateados para regresión (reshape): {years_reshaped}")

    # Construir la matriz de características polinómicas (X)
    X_poly = polynomial_features.fit_transform(years_reshaped)
    print(f"Matriz de características polinómicas (X):\n{X_poly}")

    # Ajustar el modelo lineal con las características polinómicas
    linear_model = LinearRegression()
    linear_model.fit(X_poly, valores)
    print(f"Modelo ajustado. Coeficientes del polinomio: {linear_model.coef_}")
    print(f"Término independiente (intercepto): {linear_model.intercept_}")

    # Mostrar la ecuación polinómica
    equation = f"{linear_model.intercept_:.2f} "
    for i in range(1, len(linear_model.coef_)):
        equation += f"+ ({linear_model.coef_[i]:.2f} * x^{i}) "
    print(f"Ecuación del polinomio ajustado: {equation}")

    # Define los años futuros a predecir (2024 a 2030)
    future_years = np.arange(2024, 2031).reshape(-1, 1)
    print(f"Años futuros a predecir: {future_years.flatten()}")

    # Construir las características polinómicas para los años futuros
    X_future_poly = polynomial_features.fit_transform(future_years)
    print(f"Matriz de características polinómicas para años futuros (X):\n{X_future_poly}")

    # Realiza las predicciones para los años futuros
    predicciones = linear_model.predict(X_future_poly)
    print(f"Predicciones calculadas: {predicciones}")

    # Devuelve los años, valores originales, años futuros, y las predicciones
    return years, valores, future_years, predicciones

# Función para mostrar un gráfico de los datos y las predicciones
def mostrar_grafico(years, valores, future_years, predicciones, concepto):
    # Crear una gráfica de los datos originales
    plt.plot(years, valores, 'bo-', label="Datos Originales")

    # Añadir las predicciones a la gráfica
    plt.plot(future_years, predicciones, 'ro--', label="Predicciones 2024-2030")

    # Etiquetas y título
    plt.xlabel("Año")
    plt.ylabel("Valores")
    plt.title(f"Regresión Polinómica para {concepto}")

    # Añadir leyenda
    plt.legend()

    # Mostrar la gráfica
    plt.show()

# Función principal para ejecutar el análisis
def main():
    # Definir la ruta del archivo CSV
    file_path = r'C:\Users\Rudy Gregorio\OneDrive\Desktop\Tareas\Semestre 6\Método Númericos\Proyecto 1\situacion_financiera.csv'
    
    # Cargar los datos desde el archivo CSV
    df = cargar_datos(file_path)

    if df is not None:
        # Mostrar al usuario los conceptos disponibles en el archivo
        print("Conceptos disponibles:")
        for concepto in df['Concepto']:
            print(f"- {concepto}")

        # Solicitar al usuario que ingrese el nombre del concepto que desea analizar
        concepto = input("\nIngrese el nombre del concepto que desea analizar exactamente como aparece: ")

        # Verificar si el concepto ingresado existe en el archivo
        if concepto in df['Concepto'].values:
            # Realizar la regresión polinómica y obtener las estimaciones
            years, valores, future_years, predicciones = estimar_regresion_polinomica(df, concepto)
            
            if years is not None:
                # Mostrar las estimaciones en la consola antes de la gráfica
                for i, year in enumerate(range(2024, 2031)):
                    print(f"Estimación para {concepto} en {year}: {predicciones[i]:.2f}")

                # Mostrar la gráfica con los datos y las predicciones
                mostrar_grafico(years, valores, future_years, predicciones, concepto)
        else:
            # Mostrar un mensaje de error si el concepto no se encuentra
            print("Concepto no encontrado. Por favor, verifique la ortografía y vuelva a intentarlo.")

# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
