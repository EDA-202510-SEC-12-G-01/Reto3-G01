import time
import sys
import os
import tabulate as tb
from datetime import datetime
import tabulate as tb


default_limit=100000
sys.setrecursionlimit(default_limit*10)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataStructures.List.list_iterator import iterator
from App import logic
from DataStructures.List import array_list as al

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return logic.new_logic()

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control, archivo):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    time, size, reports_recortado = logic.load_data(control, archivo)
    print()
    print("INICIANDO LA CARGA DE DATOS")
    print("========================================================================================================")
    print("SE CARGARON LOS DATOS CORRECTAMENTE")
    print("Tiempo de ejecución en ms: ", time)
    print("Cantidad de reportes cargados: ", size)
    print("INFORMACIÓN DE LOS CINCO PRIMEROS Y CINCO ÚLTIMOS REPORTES CARGADOS.")
    print(tb.tabulate(iterator(reports_recortado), headers= 'keys' , tablefmt= "fancy_grid"))
    print()


def print_data(control, id):
    reporte = logic.get_data(control, id)
    if not reporte:
        print(f"No se encontró un reporte con ID: {id}")
        return

    info = logic.extract_info(reporte, "carga_datos")

    print("==== Información del Reporte ====")
    print(f"ID (DR_NO): {info['DR_NO']}")
    print(f"Fecha Reportada (Date Rptd): {datetime.fromtimestamp(info['Date Rptd'])}")
    print(f"Fecha de Ocurrencia (DATE OCC): {datetime.fromtimestamp(info['DATE OCC'])}")
    print(f"Nombre del Área: {info['AREA NAME']}")
    print(f"Código de Crimen (Crm Cd): {info['Crm Cd']}")
    print("=================================")

def print_req_1(control):
    fecha_inicial = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ")
    start_time = logic.get_time()
    resultado = logic.req_1(control, fecha_inicial, fecha_final)
    end_time = logic.get_time()
    duracion = logic.delta_time(start_time, end_time)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms: ", duracion)
    print(tb.tabulate(iterator(resultado), headers="keys", tablefmt="fancy_grid"))
    print()


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    area_ciudad = input("Ingrese el nombre del área a consultar: ")
    num_crimenes = int(input("Ingrese el número de crímenes reportados a mostrar: "))
    start_time = logic.get_time()
    total_crimenes, respuesta = logic.req_3(control, num_crimenes, area_ciudad)
    end_time = logic.get_time()
    duracion = logic.delta_time(start_time, end_time)
    cantidad_mostrada = al.size(respuesta)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms:", duracion)
    print(f"Crímenes registrados en el área '{area_ciudad}': {total_crimenes}")
    print(f"Mostrando los {cantidad_mostrada} crímenes más recientes:")
    print()
    tabla = []
    for i in range(cantidad_mostrada):
        crimen = al.get_element(respuesta, i)
        fila = {
            "DR_NO":        crimen["DR_NO"],
            "DATE OCC":     crimen["DATE OCC"],
            "TIME OCC":     crimen["TIME OCC"],
            "AREA":         crimen["AREA"],
            "Rpt Dist No":  crimen["Rpt Dist No"],
            "Part 1-2":     crimen["Part 1-2"],
            "Crm Cd":       crimen["Crm Cd"],
            "Status":       crimen["Status"],
            "LOCATION":     crimen["LOCATION"],
        }
        tabla.append(fila)
    print(tb.tabulate(tabla, headers="keys", tablefmt="fancy_grid"))
    print()


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    sexo = input("Ingrese el sexo (M/F) a consultar: ").upper()
    mes = int(input("Ingrese el mes (1-12) a consultar: "))
    num_areas = int(input("Ingrese el número de áreas a mostrar: "))
    start_time = logic.get_time()
    respuesta = logic.req_6(control, num_areas, sexo, mes)
    end_time = logic.get_time()
    duracion = logic.delta_time(start_time, end_time)
    cantidad_mostrada = al.size(respuesta)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms:", duracion)
    print(f"Mostrando las {cantidad_mostrada} áreas más seguras (con menos crímenes) en el mes {mes}:")
    print()
    tabla = []
    for i in range(cantidad_mostrada):
        area = al.get_element(respuesta, i)
        fila = {
            "AREA NAME":     area["AREA NAME"],
            "TOTAL CRIMES EN EL MES":  area["total_crimes"],
            "AÑOS CON CRIMENES": ", ".join([f"{anio}: {count}" for count, anio in area["years"]])
        }
        tabla.append(fila)
    print(tb.tabulate(tabla, headers="keys", tablefmt="fancy_grid"))
    print()


def print_req_7(control):
    sexo = input("Ingrese el sexo (M/F) a consultar: ").upper()
    edad_inicial = int(input("Ingrese la edad mínima a consultar: "))
    edad_final = int(input("Ingrese la edad máxima a consultar: "))
    num_areas = int(input("Ingrese el número de áreas a mostrar: "))

    start_time = logic.get_time()
    respuesta = logic.req_7(control, num_areas, sexo, edad_inicial, edad_final)
    end_time = logic.get_time()
    duracion = logic.delta_time(start_time, end_time)
    cantidad_mostrada = al.size(respuesta)

    print()
    print("=" * 100)
    print("Tiempo de ejecución en ms:", duracion)
    print(f"Mostrando los {cantidad_mostrada} crímenes reportados para el sexo {sexo} en el rango de edades {edad_inicial}-{edad_final}:")
    print()

    tabla = []

    def dividir_lineas(pares, tipo, largo_linea=80):
        texto = ""
        linea = ""
        for count, valor in pares:
            fragmento = f"{count} crímenes, {tipo} {valor}"
            if len(linea) + len(fragmento) + 2 > largo_linea:
                texto += linea.rstrip(", ") + "\n"
                linea = fragmento + ", "
            else:
                linea += fragmento + ", "
        texto += linea.rstrip(", ")
        return texto

    for i in range(cantidad_mostrada):
        crimen = al.get_element(respuesta, i)
        fila = {
            "Crm Cd":       crimen["Crm Cd"],
            "TOTAL CRIMES": crimen["total"],
            "POR EDAD":     dividir_lineas(crimen["por_edad"], "edad"),
            "POR AÑO":      dividir_lineas(crimen["por_anio"], "año")
        }
        tabla.append(fila)

    print(tb.tabulate(tabla, headers="keys", tablefmt="fancy_grid", stralign="left", numalign="right"))
    print()

def print_req_8(control):
    area_interes = input("Ingrese el nombre del área de interés: ")
    crimenes_consultados = int(input("Ingrese el número de crímenes a consultar: "))
    tipo_crimen = input("Ingrese el código del crimen (Crm Cd): ")
    start_time = logic.get_time()
    cercanos, lejanos = logic.req_8(control, crimenes_consultados, area_interes, tipo_crimen)
    end_time = logic.get_time()
    duracion = logic.delta_time(start_time, end_time)
    print()
    print("========================================================================================================")
    print("Tiempo de ejecución en ms: ", duracion)
    print(f"Mostrando los {al.size(cercanos)} crímenes más cercanos:")
    print()
    tabla_cercanos = []
    for pareja in cercanos:
        fila = {
            "Crm Cd": pareja["Crm Cd"],
            "Area otra": pareja["Area otra"],
            "Fecha crimen area interes": datetime.fromtimestamp(pareja["Fecha crimen area interes"]).strftime("%Y-%m-%d %H:%M:%S"),
            "Fecha crimen otra area": datetime.fromtimestamp(pareja["Fecha crimen otra area"]).strftime("%Y-%m-%d %H:%M:%S"),
            "Distancia (km)": pareja["Distancia (km)"]
        }
        tabla_cercanos.append(fila)
    print(tb.tabulate(tabla_cercanos, headers="keys", tablefmt="fancy_grid"))
    print(f"\nMostrando los {al.size(lejanos)} crímenes más lejanos:")
    print()
    tabla_lejanos = []
    for pareja in lejanos:
        fila = {
            "Crm Cd": pareja["Crm Cd"],
            "Area otra": pareja["Area otra"],
            "Fecha crimen area interes": datetime.fromtimestamp(pareja["Fecha crimen area interes"]).strftime("%Y-%m-%d %H:%M:%S"),
            "Fecha crimen otra area": datetime.fromtimestamp(pareja["Fecha crimen otra area"]).strftime("%Y-%m-%d %H:%M:%S"),
            "Distancia (km)": pareja["Distancia (km)"]
        }
        tabla_lejanos.append(fila)
    print(tb.tabulate(tabla_lejanos, headers="keys", tablefmt="fancy_grid"))
    print()


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            archivo = seleccionar_archivo()
            load_data(control, archivo)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

def seleccionar_archivo():
    print("Escoja el archivo a cargar")
    print("0- Crime_in_LA_1.csv")
    print("1- Crime_in_LA_20.csv")
    print("2- Crime_in_LA_40.csv")
    print("3- Crime_in_LA_60.csv")
    print("4- Crime_in_LA_80.csv")
    print("5- Crime_in_LA_100.csv")
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 0:
        return "Crime_in_LA_1.csv"
    elif int(inputs) == 1:
        return "Crime_in_LA_20.csv"
    elif int(inputs) == 2:
        return "Crime_in_LA_40.csv"
    elif int(inputs) == 3:
        return "Crime_in_LA_60.csv"
    elif int(inputs) == 4:
        return "Crime_in_LA_80.csv"
    elif int(inputs) == 5:
        return "Crime_in_LA_100.csv"
    else:
        print("Opción errónea, vuelva a elegir.\n")
        seleccionar_archivo()