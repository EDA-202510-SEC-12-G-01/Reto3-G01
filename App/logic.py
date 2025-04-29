import time
import sys
import os
import csv
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

default_limit=1000000
sys.setrecursionlimit(default_limit*10)

from DataStructures.List import array_list as al
from DataStructures.List.list_iterator import iterator
from DataStructures.Tree import binary_search_tree as rbt
from DataStructures.List import single_linked_list as sll

data_dir = os.path.dirname(os.path.realpath("__file__")) + "\\Data\\"

csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "report_crimes": al.new_list(), 
        "report_crimes_Date_Rptd": rbt.new_map(), 
        "report_crimes_DATE_OCC": rbt.new_map(),
        "report_crimes_AREA": rbt.new_map(),
        "report_crimes_Vict_Age": rbt.new_map()
        }
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    star_time = get_time()
    report_crimes = catalog["report_crimes"]
    report_crimes_Date_Rptd = catalog["report_crimes_Date_Rptd"]
    report_crimes_DATE_OCC = catalog["report_crimes_DATE_OCC"]
    report_crimes_AREA = catalog["report_crimes_AREA"]
    report_crimes_Vict_Age = catalog["report_crimes_Vict_Age"]
    file_path = data_dir + filename
    with open(file_path, encoding="utf-8") as file:
        input_file = csv.DictReader(file)
        for row in input_file:
            row["DR_NO"] = int(row["DR_NO"])
            row["TIME OCC"] = int(row["TIME OCC"])
            row["AREA"] = int(row["AREA"])
            row["Rpt Dist No"] = int(row["Rpt Dist No"])
            row["Part 1-2"] = int(row["Part 1-2"])
            row["Crm Cd"] = int(row["Crm Cd"])
            row["Vict Age"] = int(row["Vict Age"])
            row["Premis Cd"] = float(row["Premis Cd"])
            row["LAT"] = float(row["LAT"])
            row["LON"] = float(row["LON"])
            row["Date Rptd"] = datetime.strptime(row["Date Rptd"], "%m/%d/%Y %I:%M:%S %p").timestamp()
            row["DATE OCC"] = datetime.strptime(row["DATE OCC"], "%m/%d/%Y %I:%M:%S %p").timestamp()
            
            if not rbt.contains(report_crimes_Date_Rptd, row["Date Rptd"]):
                lista1 = al.new_list()
                al.add_last(lista1, row)
                rbt.put(report_crimes_Date_Rptd, row["Date Rptd"], lista1)
            else:
                al.add_last(rbt.get(report_crimes_Date_Rptd, row["Date Rptd"]), row)
                
            if not rbt.contains(report_crimes_DATE_OCC, row["DATE OCC"]):
                lista2 = al.new_list()
                al.add_last(lista2, row)
                rbt.put(report_crimes_DATE_OCC, row["DATE OCC"], lista2)
            else:
                al.add_last(rbt.get(report_crimes_DATE_OCC, row["DATE OCC"]), row)
                
            if not rbt.contains(report_crimes_AREA, row["AREA"]):
                lista3 = al.new_list()
                al.add_last(lista3, row)
                rbt.put(report_crimes_AREA, row["AREA"], lista3)
            else:
                al.add_last(rbt.get(report_crimes_AREA, row["AREA"]), row)
            
            if not rbt.contains(report_crimes_Vict_Age, row["Vict Age"]):
                lista4 = al.new_list()
                al.add_last(lista4, row)
                rbt.put(report_crimes_Vict_Age, row["Vict Age"], lista4)
            else:
                al.add_last(rbt.get(report_crimes_Vict_Age, row["Vict Age"]), row)
            al.add_last(report_crimes, row)
    end_time = get_time()
    time = delta_time(star_time, end_time)
    return round(time, 3), al.size(report_crimes), get_first_last_info(report_crimes, "carga_datos")

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    return rbt.get(catalog["report_crimes"], id)

def extract_info(report, requerimiento):
    if requerimiento == "carga_datos":
        return {
            "DR_NO": report["DR_NO"],
            "Date Rptd": report["Date Rptd"],
            "DATE OCC": report["DATE OCC"],
            "AREA NAME": report["AREA NAME"],
            "Crm Cd": report["Crm Cd"],
        }
    elif requerimiento == "requerimiento_3":
        return {
            "DR_NO": report["DR_NO"],
            "DATE OCC": report["DATE OCC"],
            "TIME OCC": report["TIME OCC"],
            "AREA": report["AREA"],
            "Rpt Dist No": report["Rpt Dist No"],
            "Part 1-2": report["Part 1-2"],
            "Crm Cd": report["Crm Cd"],
            "Status": report["Status"],
            "LOCATION": report["LOCATION"],
        }
    return report
            
def get_first_last_info(reports_list, requerimiento, num = 10):
    total = al.size(reports_list)
    new_list_return = al.new_list()       
    if total <= num:
        for i in range(total):
            rec = al.get_element(reports_list, i)
            al.add_last(new_list_return, extract_info(rec, requerimiento))
    else:
        for i in range(5):
            rec = al.get_element(reports_list, i)
            al.add_last(new_list_return, extract_info(rec, requerimiento))
        for i in range(total - 5, total):
            rec = al.get_element(reports_list, i)
            al.add_last(new_list_return, extract_info(rec, requerimiento))
    return new_list_return

def req_1(catalog, fecha_inicial, fecha_final):
    
    fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d").timestamp()
    fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d").timestamp()
    
    arbol = catalog["report_crimes_DATE_OCC"]
    lista_llaves = rbt.keys(arbol, fecha_inicial, fecha_final)
    
    lista_crimenes = al.new_list()
    for i in range(sll.size(lista_llaves)):
        elementos = sll.get_element(lista_llaves, i)
        valor_por_llave = rbt.get(arbol, elementos)
        for j in range(sll.size(valor_por_llave)):
            al.add_last(lista_crimenes,sll.get_element(valor_por_llave, j))
    
    al.merge_sort(lista_crimenes, sort_criteria_req_1_3)
    
    resultado = al.new_list()
    for c in lista_crimenes:
        al.add_last(resultado, {
            "DR_NO":     c["DR_NO"],
            "DATE OCC":  c["DATE OCC"],
            "TIME OCC":  c["TIME OCC"],
            "AREA NAME": c["AREA NAME"],
            "Crm Cd":    c["Crm Cd"],
            "LOCATION": c["LOCATION"]
        })

    return resultado

def sort_criteria_req_1_3(r1, r2):
    if r1["DATE OCC"] > r2["DATE OCC"]:
        return True
    elif r1["DATE OCC"] < r2["DATE OCC"]:
        return False
    else:
        return r1["AREA"] > r2["AREA"]


def req_2(catalog):

    pass


def req_3(catalog, num_crimenes, area_ciudad):

    reportes_area = al.new_list()
    all_crimes = catalog["report_crimes"]

    for i in range(al.size(all_crimes)):
        crimen = al.get_element(all_crimes, i)
        if crimen["AREA NAME"].lower() == area_ciudad.lower():
            al.add_last(reportes_area, crimen)

    al.merge_sort(reportes_area, sort_criteria_req_1_3)

    respuesta = al.new_list()
    total_crimenes = al.size(reportes_area)

    for i in range(min(num_crimenes, total_crimenes)):
        crimen = al.get_element(reportes_area, i)
        al.add_last(respuesta, extract_info(crimen, "requerimiento_3"))

    return total_crimenes, respuesta



def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

catalog = new_logic()

load_data(catalog, "Crime_in_LA_100.csv")

print(catalog)


