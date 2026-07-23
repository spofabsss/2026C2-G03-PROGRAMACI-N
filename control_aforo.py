"""Reto integrador: control de ingreso al Anfiteatro del CENAC.

Nombre del estudiante: Fabiana Alpizar Lopez
Fecha:
Contexto:
El Anfiteatro del Centro Nacional de la Cultura (CENAC), en Costa Rica, tiene
capacidad máxima para 700 personas.
Fuente: https://si.cultura.cr/infraestructura/anfiteatro-del-centro-nacional-de-cultura

Objetivo:
Registre los grupos que desean entrar y evite que la ocupación supere 700.

Reglas:
- Cada entrada es un grupo completo. No se permite entrada parcial.
- Escriba "fin" para terminar.
- Acepte solo enteros mayores que cero.
- Si ocupación actual + grupo <= 700, acepte el grupo.
- Si ocupación actual + grupo > 700, rechace el grupo.

Requisitos:
- Use listas para grupos aceptados y rechazados.
- Use while, for, condicionales y try-except.
- No use menú, while True, funciones propias, CSV, listas anidadas ni
  comprensiones de listas.

Después de cada grupo válido, muestre:
- Mensaje de aceptación o rechazo.
- Ocupación actual.
- Espacios disponibles.

Al finalizar, muestre:
- Grupos aceptados, grupos rechazados y personas admitidas.
- Capacidad máxima, espacios disponibles y porcentaje de ocupación.
- Grupo aceptado más pequeño y más grande, si existe alguno.
- Estado final:
  menos de 560 = disponibilidad normal,
  560 a 699 = ocupación preventiva,
  700 = capacidad completa.

Salida esperada:
Entradas: 650, 60, 50, fin

Grupo aceptado: ingresan 650 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo rechazado: no hay espacio para 60 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo aceptado: ingresan 50 personas.
Ocupación actual: 700
Espacios disponibles: 0

REPORTE FINAL
Grupos aceptados: 2
Grupos rechazados: 1
Personas admitidas: 700
Capacidad máxima: 700
Espacios disponibles: 0
Porcentaje de ocupación: 100.00%
Grupo aceptado más pequeño: 50
Grupo aceptado más grande: 650
Estado final: capacidad completa.



# Desarrolle su solución a partir de esta línea.

capacidad_maxima = 700
ocupacion_actual = 0

grupos_aceptados = []
grupos_rechazados = []

grupo = ""

while grupo != "fin":

    grupo = input("Ingrese la cantidad de personas del grupo (o escriba 'fin'): ")

    if grupo != "fin":

        try:
            grupo = int(grupo)

            if grupo > 0:

                if ocupacion_actual + grupo <= capacidad_maxima:

                    grupos_aceptados.append(grupo)
                    ocupacion_actual = ocupacion_actual + grupo

                    print("Grupo aceptado: ingresan", grupo, "personas.")
                    print("Ocupación actual:", ocupacion_actual)
                    print("Espacios disponibles:", capacidad_maxima - ocupacion_actual)

                else:

                    grupos_rechazados.append(grupo)

                    print("Grupo rechazado: no hay espacio para", grupo, "personas.")
                    print("Ocupación actual:", ocupacion_actual)
                    print("Espacios disponibles:", capacidad_maxima - ocupacion_actual)

            else:
                print("Debe ingresar un número entero mayor que cero.")

        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero o 'fin'.")

print("\nREPORTE FINAL")

print("Grupos aceptados:", len(grupos_aceptados))
print("Grupos rechazados:", len(grupos_rechazados))
print("Personas admitidas:", ocupacion_actual)
print("Capacidad máxima:", capacidad_maxima)
print("Espacios disponibles:", capacidad_maxima - ocupacion_actual)

porcentaje = (ocupacion_actual / capacidad_maxima) * 100
print("Porcentaje de ocupación:", format(porcentaje, ".2f"), "%", sep="")

if len(grupos_aceptados) > 0:

    grupo_menor = grupos_aceptados[0]
    grupo_mayor = grupos_aceptados[0]

    for grupo in grupos_aceptados:

        if grupo < grupo_menor:
            grupo_menor = grupo

        if grupo > grupo_mayor:
            grupo_mayor = grupo

    print("Grupo aceptado más pequeño:", grupo_menor)
    print("Grupo aceptado más grande:", grupo_mayor)

if ocupacion_actual < 560:
    print("Estado final: disponibilidad normal")

elif ocupacion_actual < 700:
    print("Estado final: ocupación preventiva")

else:
    print("Estado final: capacidad completa")
