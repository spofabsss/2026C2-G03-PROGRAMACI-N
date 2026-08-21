import pandas as pd
import matplotlib.pyplot as plt


# Cargar el archivo CSV
df = pd.read_csv(
    r"c:\Users\Usuario\Downloads\Población total por condición de actividad y tasas..csv",
    sep=";",
    skiprows=5
)


# Convertir la fecha a formato de fecha
df["Fecha"] = pd.to_datetime(df["Fecha"])


# Convertir columnas de población a números
columnas_numericas = [
    "Población Total (PT)",
    "Población Total de 15 años o más",
    "Fuerza de trabajo (FT)",
    "Ocupados (PO)",
    "Población que busca trabajo (desocupado)"
]

for columna in columnas_numericas:
    df[columna] = df[columna].str.replace(",", "").astype(float)


# Revisar si existen datos vacíos
print("\nDatos vacíos:")
print(df.isnull().sum())


# Lista de indicadores
indicadores = [
    "Población Total (PT)",
    "Población Total de 15 años o más",
    "Fuerza de trabajo (FT)",
    "Ocupados (PO)",
    "Población que busca trabajo (desocupado)",
    "Tasa neta de participación (FT/PT 15 años o más)",
    "Tasa de ocupación (PO/PT 15 años o más)",
    "Tasa de desempleo abierto",
    "Tasa de subempleo"
]


# Diccionario con algunos datos principales
datos = {
    "poblacion_total": "Población Total (PT)",
    "fuerza_trabajo": "Fuerza de trabajo (FT)",
    "ocupados": "Ocupados (PO)",
    "desempleados": "Población que busca trabajo (desocupado)"
}


# Función para mostrar estadísticas
def mostrar_estadisticas(datos):
    promedio = datos["Tasa de desempleo abierto"].mean()
    maximo = datos["Tasa de desempleo abierto"].max()
    minimo = datos["Tasa de desempleo abierto"].min()

    print("\n------ ESTADÍSTICAS DE DESEMPLEO ------")
    print(f"Promedio de desempleo: {promedio:.2f}%")
    print(f"Tasa máxima de desempleo: {maximo:.2f}%")
    print(f"Tasa mínima de desempleo: {minimo:.2f}%")


# Menú principal
while True:

    print("\n------ ANÁLISIS DE POBLACIÓN Y EMPLEO EN COSTA RICA ------")
    print("1. Mostrar datos")
    print("2. Consultar un indicador")
    print("3. Ver estadísticas")
    print("4. Graficar")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(df.head())

    elif opcion == "2":
        print("\nIndicadores disponibles:")
        print("1. Población total")
        print("2. Fuerza de trabajo")
        print("3. Ocupados")
        print("4. Desempleados")

        indicador = input("Seleccione un indicador: ")

        if indicador == "1":
            print(df[["Fecha", "Población Total (PT)"]])

        elif indicador == "2":
            print(df[["Fecha", "Fuerza de trabajo (FT)"]])

        elif indicador == "3":
            print(df[["Fecha", "Ocupados (PO)"]])

        elif indicador == "4":
            print(df[["Fecha", "Población que busca trabajo (desocupado)"]])

        else:
            print("Opción inválida.")

    elif opcion == "3":
        mostrar_estadisticas(df)

 # OPCIÓN 4: Mostrar gráfico
    elif opcion == "4":

        # Crear la figura
        plt.figure(figsize=(8, 4))

        # Agregar los datos
        plt.plot(df["Fecha"], df["Tasa de desempleo abierto"])

        # Personalizar el gráfico
        plt.title("Tasa de desempleo en Costa Rica")
        plt.xlabel("Fecha")
        plt.ylabel("Porcentaje")

        # Ajustar y mostrar
        plt.tight_layout()
        plt.show()
    
    
    elif opcion == "5":
        print("Análisis finalizado.")
        break

    else:
        print("Opción inválida.")