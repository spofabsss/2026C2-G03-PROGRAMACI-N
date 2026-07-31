"""Programa principal del proyecto modular BCCR."""
print ("Inicio el programa")
from lectura_datos import cargar_tabla_bccr 
from limpieza_datos import limpiar_datos

def ejecutar (): 
    """Cargar los datos y presentar el menu del sistema"""
    datos_crudos = cargar_tabla_bccr()
    datos= limpiar_datos (datos_crudos)
    
    print (datos.head())
    while True:
        print ("\nPROYECTO DE ANALISIS BCCR")
        print ("1. Mostrar primeras 10 entidades limpias")
    
    if __name__ == "__main__":
        ejecutar ()