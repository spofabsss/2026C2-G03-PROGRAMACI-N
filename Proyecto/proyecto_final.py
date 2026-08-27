#PROYECTO FINAL POR FABIANA ALPIZAR LOPEZ


import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# 1. CARGA DEL ARCHIVO CSV
# ---------------------------------------------------------

# Se intenta cargar el archivo descargado del BCCR
# Si el archivo no existe o tiene algún problema, se muestra un mensaje de error

try:
    df = pd.read_csv(
        r"c:\Users\Usuario\Downloads\Población total por condición de actividad y tasas..csv",
        sep=";",
        skiprows=5
    )

    print("Archivo cargado correctamente.")

except FileNotFoundError:
    print("Error: no se encontró el archivo CSV.")
    exit()

except Exception:
    print("Error: no se pudo leer el archivo.")
    exit()


# ---------------------------------------------------------
# 2. LIMPIEZA Y CONVERSIÓN DE DATOS
# ---------------------------------------------------------

# Convertir la columna Fecha a formato de fecha
df["Fecha"] = pd.to_datetime(df["Fecha"])


# Algunas columnas de población vienen como texto.
# Primero se eliminan las comas y luego se convierten a números.

columnas_numericas = [
    "Población Total (PT)",
    "Población Total de 15 años o más",
    "Fuerza de trabajo (FT)",
    "Ocupados (PO)",
    "Población que busca trabajo (desocupado)"
]

for columna in columnas_numericas:
    df[columna] = df[columna].str.replace(",", "").astype(float)


# Revisar si existen datos vacíos.
print("\nDatos vacíos:")
print(df.isnull().sum())


# Revisar si existen datos duplicados
print("\nDatos duplicados:")
print(df.duplicated().sum())


# Eliminar registros duplicados si existen.
df = df.drop_duplicates()


# ---------------------------------------------------------
# 3. ESTRUCTURAS DE DATOS
# ---------------------------------------------------------

# Lista con todos los indicadores que el usuario puede consultar.

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


# Diccionario con algunos de los datos principales.
# Se utiliza en la opción 1 del menú.

datos = {
    "poblacion_total": "Población Total (PT)",
    "fuerza_trabajo": "Fuerza de trabajo (FT)",
    "ocupados": "Ocupados (PO)",
    "desempleados": "Población que busca trabajo (desocupado)"
}


# ---------------------------------------------------------
# 4. FUNCIÓN PARA EL ANÁLISIS ESTADÍSTICO
# ---------------------------------------------------------

def mostrar_estadisticas(datos):
    """Calcula y muestra estadísticas básicas de desempleo."""

    promedio = datos["Tasa de desempleo abierto"].mean()
    maximo = datos["Tasa de desempleo abierto"].max()
    minimo = datos["Tasa de desempleo abierto"].min()

    print("\n------ ESTADÍSTICAS DE DESEMPLEO ------")
    print(f"Promedio de desempleo: {promedio:.2f}%")
    print(f"Tasa máxima de desempleo: {maximo:.2f}%")
    print(f"Tasa mínima de desempleo: {minimo:.2f}%")


# ---------------------------------------------------------
# 5. MENÚ PRINCIPAL
# ---------------------------------------------------------

# El ciclo se repite hasta que el usuario seleccione la opción Salir.

while True:

    print("\n------ ANÁLISIS DE POBLACIÓN Y EMPLEO EN COSTA RICA ------")
    print("1. Mostrar datos")
    print("2. Consultar un indicador")
    print("3. Ver estadísticas")
    print("4. Graficar")
    print("5. Comparar períodos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    
    # INICIO DE LAS OPCIONES DEL MENÚ (1-6)
    
    # -----------------------------------------------------
    # OPCIÓN 1: Mostrar datos principales
    # -----------------------------------------------------

    if opcion == "1":

        print("\n------ DATOS PRINCIPALES ------")

        # Recorrer el diccionario y mostrar los primeros datos
        # de cada indicador principal.

        for nombre, columna in datos.items():
            print("\n", nombre)
            print(df[["Fecha", columna]].head())


    # -----------------------------------------------------
    # OPCIÓN 2: Consultar un indicador
    # -----------------------------------------------------

    elif opcion == "2":

        print("\n------ INDICADORES DISPONIBLES ------")

        # Mostrar los indicadores de la lista utilizando un ciclo for.

        numero = 1

        for indicador in indicadores:
            print(numero, "-", indicador)
            numero = numero + 1

        seleccion = input("Seleccione el número del indicador: ")

        # Convertir la opción del usuario de texto a número.
        seleccion = int(seleccion)

        # Verificar que el número esté dentro de las opciones disponibles.

        if seleccion >= 1 and seleccion <= len(indicadores):

            indicador_elegido = indicadores[seleccion - 1]

            print("\nIndicador seleccionado:")
            print(indicador_elegido)

            print(df[["Fecha", indicador_elegido]])

        else:
            print("Indicador inválido.")


    # -----------------------------------------------------
    # OPCIÓN 3: Mostrar estadísticas
    # -----------------------------------------------------

    elif opcion == "3":

        mostrar_estadisticas(df)


    # -----------------------------------------------------
    # OPCIÓN 4: Mostrar gráfico
    # -----------------------------------------------------

    elif opcion == "4":

        # Crear la figura.
        plt.figure(figsize=(8, 4))

        # Agregar la fecha y la tasa de desempleo al gráfico.
        plt.plot(df["Fecha"], df["Tasa de desempleo abierto"])

        # Personalizar el gráfico.
        plt.title("Tasa de desempleo en Costa Rica")
        plt.xlabel("Fecha")
        plt.ylabel("Porcentaje")

        # Ajustar y mostrar el gráfico.
        plt.tight_layout()
        plt.show()


    # -----------------------------------------------------
    # OPCIÓN 5: Comparar dos períodos
    # -----------------------------------------------------

    elif opcion == "5":

        print("\n------ COMPARAR PERÍODOS ------")

        # Solicitar las dos fechas que se desean comparar.
        fecha1 = input("Escriba la primera fecha (AAAA-MM-DD): ")
        fecha2 = input("Escriba la segunda fecha (AAAA-MM-DD): ")

        # Buscar las fechas dentro del DataFrame.
        dato1 = df[df["Fecha"] == fecha1]
        dato2 = df[df["Fecha"] == fecha2]

        # Verificar que ambas fechas existan.
        if not dato1.empty and not dato2.empty:

            print("\nPrimera fecha:")
            print(
                dato1[[
                    "Fecha",
                    "Tasa de desempleo abierto",
                    "Tasa de ocupación (PO/PT 15 años o más)"
                ]]
            )

            print("\nSegunda fecha:")
            print(
                dato2[[
                    "Fecha",
                    "Tasa de desempleo abierto",
                    "Tasa de ocupación (PO/PT 15 años o más)"
                ]]
            )

        else:
            print("Una de las fechas no fue encontrada.")


    # -----------------------------------------------------
    # OPCIÓN 6: Salir
    # -----------------------------------------------------

    elif opcion == "6":

        print("Análisis finalizado.")
        break


    # Si el usuario escribe una opción que no existe.
    else:
        print("Opción inválida.")