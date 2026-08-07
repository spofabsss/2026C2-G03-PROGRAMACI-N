"""Programa principal del proyecto modular BCCR."""

from lectura_datos import cargar_tabla_bccr, mostrar_top_10 
from limpieza_datos import filtrar_diferencial_alto, limpiar_datos

def ejecutar (): 
    """Cargar los datos y presentar el menu del sistema"""
    datos_crudos = cargar_tabla_bccr()
    datos= limpiar_datos (datos_crudos)
    print (datos.head())

if __name__ == "__main__":
    ejecutar()
    
    while True: 
        print("\nPROYECTO DE ÁNALISIS BCCR")
        print("1. Mostrar primeras 10 entidades limpias.")
        print("2. Promedio por tipo entidad.")
        print("3. Mostrar entidades financieras con diferencial mayor al promedio.")
        print("4. Mostrar lista entidades y exportar CSV.")
        print("5. Graficar")
        print("6. Salir")
        
        opcion = input("Seleccione un opción: ").strip()
        if opcion == "1":
            seleccion = ["ENTIDAD", "COMPRA", "VENTA", "DIFERENCIAL"]
            
            print(mostrar_top_10(datos))
        elif opcion == "2":
            
        
        elif opcion == "3":
        print("Entidades con diferencial mayor al promedio:")
            entidades_altas = filtrar_diferencial_alto(datos)
            print(mostrar_top_10(entidades_altas))
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Graficando ...")
        elif opcion == "6":
            input("Análisis finalizado. Presione enter para salir ...")
            break
        else:
            print("Opción inválida. Escriba un número del 1 al 6.")
        input("\nPresione enter para continuar...\n")
if __name__ == "__main__":
    ejecutar()