"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes


def calcular_total(lista_ventas):
    """Recibo una lista, la sumo y retorno el total."""
    return sum(lista_ventas)

def calcular_promedio(lista_ventas):
    """Retorna el promedio de las ventas de la lista ventas"""
    return sum(lista_ventas) / len(lista_ventas)

def calcular_porcentaje(total_ventas, meta): # total_ventas = total de ventas del emprendimeinto
    """Calcula el procentaje de cumplimiento de la meta"""
    return total_ventas / meta * 100

def calcular_clasificacion(porcentaje_logro):
    """"Clasifica el emprendimiento según porcentaje de cumplimiento de meta de ventas."""
    if porcentaje_logro >= 100:
        clasificacion_empredimiento = "Meta alcanzada, emprendimiento rentable"
    elif porcentaje_logro >= 80:
        clasificacion_empredimiento = "Observación, no se logró la meta."
    else:
        clasificacion_empredimiento = "ADVERTENCIA, problemas de rentabilidad. URGE ATENCIÓN."
    return clasificacion_empredimiento

def imprimir_reporte(reporte):
    """Imprime el reorte final de ventas por emprendimiento"""
    print("\nREPORTE FINAL")
    print("-" * 60)
    for fila in reporte:
        print(f"Empredimiento: {fila["nombre"].upper()}")
        print(f"Provincia: {fila["provincia"]}")
        print(f"Tipo: {fila["tipo"]}")
        
        print(f"Total semanal: ₡{fila["total"]:,.2f}")
        print(f"Promedio diario: ₡{fila["promedio"]:,.2f}")
        print(f"Porcentaje cumplimiento: {fila["porcentaje"]:,.0f}%")
        print(f"Estado: {fila["estado"]}")
        print("-" * 60)
    print(f"Cantidad de emprendimientos: {len(reporte)}")
    
#print("Cantidad de sedes:", len(sedes))
#print(type(sedes), "vrs", type(sedes[0]))
#print("Datos por sede:", sedes[0].keys())
#print("\nPrimer emprendimiento:", sedes[0]["nombre"])


reporte = []
provincias = set()
#FALTA GENTE

for empredimiento in sedes:
    #empredimiento = sedes[0]  # Extraigo el primer empredimeinto de la lista
    ventas = empredimiento["ventas"]
    meta = empredimiento["meta"]

    total_emprendimiento = calcular_total(ventas)
    promedio_emprendiemto = calcular_porcentaje(total_emprendimiento, meta)
    promedio_diario = calcular_promedio(ventas)
    clasificacion = calcular_clasificacion(promedio_emprendiemto)


    provincias.add(empredimiento["provincia"]) # Crea la colección sinb duplicar valores
    
    #print("\nEmprendimiento:", empredimiento["nombre"])
    #print("Total ventas:", total_emprendimiento)
    #print("Porcentaje logro:", promedio_emprendiemto)
    #print("Promedio diario:", promedio_diario)
    #print("Análisis de emprendimiento:", clasificacion)
    reporte.append(
        {
            "nombre": empredimiento["nombre"],
            "provincia": empredimiento["provincia"],
            "tipo": empredimiento["tipo"],
            "total": total_emprendimiento,
            "promedio": promedio_diario,
            "porcentaje": promedio_emprendiemto,
            "estado": clasificacion
            
        }
    )
#AL FINALIZAR FOR
imprimir_reporte(reporte)

#print(reporte)
print(provincias)