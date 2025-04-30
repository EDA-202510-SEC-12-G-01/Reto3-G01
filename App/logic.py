import time
import sys
import os
import csv
from datetime import datetime
import math
import tabulate as tb

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

default_limit=1000000
sys.setrecursionlimit(default_limit*10)

from DataStructures.List.list_iterator import iterator
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as al
from DataStructures.Map import map_separate_chaining as sc

data_dir = os.path.dirname(os.path.realpath("__file__")) + "\\Data\\"

csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "report_crimes": al.new_list(), 
        "report_crimes_Date_Rptd": bst.new_map(), 
        "report_crimes_DATE_OCC": bst.new_map(),
        "report_crimes_AREA": bst.new_map(),
        "report_crimes_Vict_Age": bst.new_map()
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
            row["LOCATION"] = " ".join(row["LOCATION"].replace("\n","").replace("\t","").split())
            
            if not bst.contains(report_crimes_Date_Rptd, row["Date Rptd"]):
                lista1 = al.new_list()
                al.add_last(lista1, row)
                bst.put(report_crimes_Date_Rptd, row["Date Rptd"], lista1)
            else:
                al.add_last(bst.get(report_crimes_Date_Rptd, row["Date Rptd"]), row)
                
            if not bst.contains(report_crimes_DATE_OCC, row["DATE OCC"]):
                lista2 = al.new_list()
                al.add_last(lista2, row)
                bst.put(report_crimes_DATE_OCC, row["DATE OCC"], lista2)
            else:
                al.add_last(bst.get(report_crimes_DATE_OCC, row["DATE OCC"]), row)
                
            if not bst.contains(report_crimes_AREA, row["AREA"]):
                lista3 = al.new_list()
                al.add_last(lista3, row)
                bst.put(report_crimes_AREA, row["AREA"], lista3)
            else:
                al.add_last(bst.get(report_crimes_AREA, row["AREA"]), row)
            
            if not bst.contains(report_crimes_Vict_Age, row["Vict Age"]):
                lista4 = al.new_list()
                al.add_last(lista4, row)
                bst.put(report_crimes_Vict_Age, row["Vict Age"], lista4)
            else:
                al.add_last(bst.get(report_crimes_Vict_Age, row["Vict Age"]), row)
            al.add_last(report_crimes, row)
    end_time = get_time()
    time = delta_time(star_time, end_time)
    return round(time, 3), al.size(report_crimes), get_first_last_info(report_crimes, "carga_datos")

def extract_info(report, requerimiento):
    if requerimiento == "carga_datos":
        return {
            "DR_NO": report["DR_NO"],
            "Date Rptd": datetime.fromtimestamp(report["Date Rptd"]).strftime("%m/%d/%Y %I:%M:%S %p"),
            "DATE OCC": datetime.fromtimestamp(report["DATE OCC"]).strftime("%m/%d/%Y %I:%M:%S %p"),
            "AREA NAME": report["AREA NAME"],
            "Crm Cd": report["Crm Cd"],
        }
    elif requerimiento == "requerimiento_1":
        return {
            "DR_NO" : report["DR_NO"],
            "DATE OCC": datetime.fromtimestamp(report["DATE OCC"]).strftime("%m/%d/%Y %I:%M:%S %p"),
            "TIME OCC" : report["TIME OCC"],
            "AREA NAME" : report["AREA NAME"],
            "Crm Cd" : report["Crm Cd"],
            "LOCATION" : report["LOCATION"]
        }
    elif requerimiento == "requerimiento_3":
        return {
            "DR_NO": report["DR_NO"],
            "DATE OCC": datetime.fromtimestamp(report["DATE OCC"]).strftime("%m/%d/%Y %I:%M:%S %p"),
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

def sort_criteria_1(element_1, element_2):
    condition = False
    if element_1["DATE OCC"] > element_2["DATE OCC"]:
        condition = True
    if element_1["DATE OCC"] == element_2["DATE OCC"]:
        if element_1['AREA'] > element_2['AREA']:
            condition = True
    return condition

def sort_criteria_2(element_1, element_2):
    condition = False
    if element_1["NUM CRIMES IC"] > element_2["NUM CRIMES IC"]:
        condition = True
    if element_1["NUM CRIMES IC"] == element_2["NUM CRIMES IC"]:
        if element_1['AREA NAME'] < element_2['AREA NAME']:
            condition = True
    return condition

def sort_criteria_3(element_1, element_2):
    condition = False
    if element_1["Num Crimes"] > element_2["Num Crimes"]:
        condition = True
    elif element_1["Num Crimes"] == element_2["Num Crimes"]:
        if element_1["Crm Cd"] < element_2["Crm Cd"]:
            condition = True
    return condition

# Funciones de consulta sobre el catálogo
def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    return bst.get(catalog["report_crimes"], id)

def filtrar_por_DATE_OCC(report_crimes_DATE_OCC, fecha_inicial, fecha_final):
    fecha_i = datetime.strptime(fecha_inicial + " 00:00:00", "%Y-%m-%d %H:%M:%S").timestamp()
    fecha_f = datetime.strptime(fecha_final + " 23:59:59", "%Y-%m-%d %H:%M:%S").timestamp()
    lista_values = bst.values(report_crimes_DATE_OCC, fecha_i, fecha_f)
    lista = al.new_list()
    for i in iterator(lista_values):
        for j in iterator(i):
            al.add_last(lista, j)
    return lista

def req_1(catalog, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 1
    """
    report_crimes_DATE_OCC = catalog["report_crimes_DATE_OCC"]
    report_crimes_DATE_OCC_list = filtrar_por_DATE_OCC(report_crimes_DATE_OCC, fecha_inicial, fecha_final)
    al.merge_sort(report_crimes_DATE_OCC_list, sort_criteria_1)
    return get_first_last_info(report_crimes_DATE_OCC_list, "requerimiento_1", 10)

def req_3(catalog, num_crimenes, area_ciudad):

    reportes_area = al.new_list()
    all_crimes = catalog["report_crimes"]

    for i in range(al.size(all_crimes)):
        crimen = al.get_element(all_crimes, i)
        if crimen["AREA NAME"].lower() == area_ciudad.lower():
            al.add_last(reportes_area, crimen)

    al.merge_sort(reportes_area, sort_criteria_req_3)

    respuesta = al.new_list()
    total_crimenes = al.size(reportes_area)

    for i in range(min(num_crimenes, total_crimenes)):
        crimen = al.get_element(reportes_area, i)
        al.add_last(respuesta, extract_info(crimen, "requerimiento_3"))

    return total_crimenes, respuesta

def sort_criteria_req_3(r1, r2):


    if r1["DATE OCC"] != r2["DATE OCC"]:

        return r1["DATE OCC"] > r2["DATE OCC"]

    elif r1["TIME OCC"] != r2["TIME OCC"]:

        return r1["TIME OCC"] > r2["TIME OCC"]

    else:

        return r1["AREA NAME"] > r2["AREA NAME"]

def req_5(catalog, N, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()
    report_crimes_DATE_OCC = catalog["report_crimes_DATE_OCC"]
    report_crimes_DATE_OCC_list = filtrar_por_DATE_OCC(report_crimes_DATE_OCC, fecha_inicial, fecha_final)
    mapa = sc.new_map(N, 2)
    first_crime = None
    last_crime = None
    for i in iterator(report_crimes_DATE_OCC_list):
        if not sc.contains(mapa, i["AREA"]):
            diccionario = {
                "AREA" : i["AREA"],
                "AREA NAME" : i["AREA NAME"],
                "NUM CRIMES IC" : 0,
                "FIRST CRIME" : None,
                "LAST CRIME" : None,
                "CRIMES" : al.new_list()
            }                
            sc.put(mapa, i["AREA"], diccionario)
        if i["Status"] == "IC":
            diccionario = sc.get(mapa, i["AREA"])
            diccionario["NUM CRIMES IC"] += 1
            lista = diccionario["CRIMES"]
            al.add_last(lista, i)    
    values = sc.value_set(mapa)
    for i in iterator(values):
        first_crime = float('inf')
        last_crime = float('-inf')   
        for j in iterator(i["CRIMES"]):
            if j["DATE OCC"] < first_crime:
                first_crime = j["DATE OCC"]
            if j["DATE OCC"] > last_crime:
                last_crime = j["DATE OCC"]
        i["FIRST CRIME"] = datetime.fromtimestamp(first_crime).strftime("%m/%d/%Y %I:%M:%S %p")
        i["LAST CRIME"] = datetime.fromtimestamp(last_crime).strftime("%m/%d/%Y %I:%M:%S %p")
        del i["CRIMES"]
    sorted_values = al.merge_sort(values, sort_criteria_2)
    if N <= al.size(sorted_values):
        sorted_values = al.sub_list(sorted_values, 0, N)
    end_time = get_time()
    time = delta_time(start_time, end_time)
    return round(time, 3), sorted_values

def req_6(catalog, num_areas, sexo, mes:int):
    crimenes = catalog["report_crimes"]
    area_crime_stats = {}
    area_dict = {}
    for i in range(al.size(crimenes)):
        crimen = al.get_element(crimenes, i)
        if crimen["AREA NAME"] not in area_dict:
            area_dict[crimen["AREA NAME"]] = crimen["AREA"]
        if crimen["Vict Sex"] != sexo:
            continue

        fecha = datetime.fromtimestamp(crimen["DATE OCC"])
        if fecha.month != mes:
            continue

        area = crimen["AREA NAME"]
        anio = fecha.year

        if area not in area_crime_stats:
            area_crime_stats[area] = {'total': 0, 'years': {}}
        
        area_crime_stats[area]['total'] += 1
        if anio not in area_crime_stats[area]['years']:
            area_crime_stats[area]['years'][anio] = 0
        area_crime_stats[area]['years'][anio] += 1

    lista_areas = al.new_list()
    for area, data in area_crime_stats.items():
        al.add_last(lista_areas,{
            "AREA": area_dict[area],
            "AREA NAME": area,
            "total_crimes": data['total'],
            "years": [(count, year) for year, count in data['years'].items()]
        })

    al.merge_sort(lista_areas, sort_criteria_req_6)

    if al.size(lista_areas) > num_areas:
        lista_limitada = al.new_list()
        for i in range(num_areas):
            al.add_last(lista_limitada, al.get_element(lista_areas, i))
            
        lista_areas = lista_limitada
    return lista_areas
    
def sort_criteria_req_6(a, b):
    
        if a["total_crimes"] != b["total_crimes"]:
            
            return a["total_crimes"] < b["total_crimes"]
        
        if len(a["years"]) != len(b["years"]):
            
            return len(a["years"]) < len(b["years"])
        
        return a["AREA NAME"] < b["AREA NAME"]



def req_7(catalog, N, sex, initial_age, final_age):
    report_by_age = catalog["report_crimes_Vict_Age"]
    rangos = bst.values(report_by_age, initial_age, final_age)
    filtrados = al.new_list()
    for sublista in iterator(rangos):
        for reg in iterator(sublista):
            if reg["Vict Sex"] == sex:
                al.add_last(filtrados, reg)

    total_counts   = {}
    age_counts     = {}
    year_counts    = {}

    for row in iterator(filtrados):
        code = row["Crm Cd"]
        total_counts[code] = total_counts.get(code, 0) + 1
        edad = row["Vict Age"]
        age_counts.setdefault(code, {})
        age_counts[code][edad] = age_counts[code].get(edad, 0) + 1
        año = datetime.fromtimestamp(row["DATE OCC"]).year
        year_counts.setdefault(code, {})
        year_counts[code][año] = year_counts[code].get(año, 0) + 1

    resultados = al.new_list()
    for code, total in total_counts.items():
        lista_edades = al.new_list()
        for edad, cnt in age_counts[code].items():
            al.add_last(lista_edades, (cnt, edad))
        lista_años = al.new_list()
        for año, cnt in year_counts[code].items():
            al.add_last(lista_años, (cnt, año))
        mapa = {
            "Crm Cd":        code,
            "Num Crimes":    total,
            "Crimes by Age": lista_edades["elements"],
            "Crimes by Year": lista_años["elements"]
        }
        al.add_last(resultados, mapa)
    sorted_list = al.merge_sort(resultados, sort_criteria_3)
    top_n = al.new_list()
    limite = min(N, al.size(sorted_list))
    for idx in range(limite):
        al.add_last(top_n, al.get_element(sorted_list, idx))
    return top_n


def req_8(catalog, crimenes_consultados, area_interes, tipo_crimen):
    
    crimenes = catalog["report_crimes"]
    crimenes_area_interes = al.new_list()
    crimenes_otras_areas = al.new_list()

    for i in range(al.size(crimenes)):
        crimen = al.get_element(crimenes, i)
        if crimen["Crm Cd"] != tipo_crimen:
            continue
        if crimen["AREA NAME"] == area_interes:
            al.add_last(crimenes_area_interes, crimen)
        else:
            al.add_last(crimenes_otras_areas, crimen)

    parejas = al.new_list()

    for i in range(al.size(crimenes_area_interes)):
        crimen_a = al.get_element(crimenes_area_interes, i)
        fecha_a = datetime.fromtimestamp(crimen_a["DATE OCC"])
        lat_a, lon_a = crimen_a["LAT"], crimen_a["LON"]

        for j in range(al.size(crimenes_otras_areas)):
            crimen_b = al.get_element(crimenes_otras_areas, j)
            fecha_b = datetime.fromtimestamp(crimen_b["DATE OCC"])
            lat_b, lon_b = crimen_b["LAT"], crimen_b["LON"]

            distancia = haversine(lat_a, lon_a, lat_b, lon_b)

            if fecha_a <= fecha_b:
                crimen_primero, crimen_segundo = crimen_a, crimen_b
                fecha_primero, fecha_segundo = fecha_a, fecha_b
            else:
                crimen_primero, crimen_segundo = crimen_b, crimen_a
                fecha_primero, fecha_segundo = fecha_b, fecha_a

            if crimen_primero["AREA NAME"] == area_interes:
                fecha_interes = fecha_primero
                fecha_otra = fecha_segundo
                area_otra = crimen_segundo["AREA NAME"]
            else:
                fecha_interes = fecha_segundo
                fecha_otra = fecha_primero
                area_otra = crimen_primero["AREA NAME"]

            pareja = {
                "Crm Cd": tipo_crimen,
                "Area otra": area_otra,
                "Fecha crimen area interes": fecha_interes,
                "Fecha crimen otra area": fecha_otra,
                "Distancia (km)": distancia
            }
            al.add_last(parejas, pareja)

    al.merge_sort(parejas, sort_criteria_req_8)

    total_parejas = al.size(parejas)
    N_cercanos = min(crimenes_consultados, total_parejas)
    N_lejanos = min(crimenes_consultados, total_parejas)

    cercanos = al.sub_list(parejas, 0, N_cercanos)
    lejanos = al.sub_list(parejas, total_parejas - N_lejanos, N_lejanos)
    
    return cercanos, lejanos

def sort_criteria_req_8(p1, p2):
    
    return p1["Distancia (km)"] < p2["Distancia (km)"]

def haversine(lat1, lon1, lat2, lon2):
    
    R = 6371 
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


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

req1 = req_7(catalog, 8, "F", 6, 18)
print(tb.tabulate(iterator(req1), headers= 'keys' , tablefmt= "fancy_grid"))