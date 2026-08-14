import pandas as pd
import matplotlib as plt

df = pd.read_csv(r"c:\Users\Usuario\Downloads\Población total por condición de actividad y tasas..csv", sep=";", skiprows=5)

print(df.head())
print(df.info())

# Convertir la fecha a formato de fecha
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Convertir las columnas de población a números
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

# Mostrar nuevamente la información
print("\nInformación después de la limpieza:")
print(df.info())

print("\nPrimeros datos:")
print(df.head())


indicadorees = [
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

datos = {
    "fechas": df["Fecha"].tolist(),
    "poblacion_total": df["Población Total (PT)"].tolist(),
    "fuerza_trabajo": df["Fuerza de trabajo (FT)"].tolist(),
    "ocupados": df["Ocupados (PO)"].tolist(),
    "desempleados": df["Población que busca trabajo (desocupado)"].tolist()
}

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
        print("Aquí podremos consultar un indicador.")

    elif opcion == "3":
        print("Aquí mostraremos estadísticas.")

    elif opcion == "4":
        print("Aquí mostraremos gráficos.")

    elif opcion == "5":
        print("Análisis finalizado.")
        break

    else:
        print("Opción inválida.")