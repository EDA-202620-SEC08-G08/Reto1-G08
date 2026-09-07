import time
import csv
import os

from DataStructures.List import array_list as lt


def new_logic(catalog):
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    
    catalog={
        "orders": lt.new_list()
    }




# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    start_time = get_time()
    csv.field_size_limit(2147483647)
    path=os.path.join("Data", "Data",filename)
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            lt.add_last(catalog["orders"], row)
    end_time = get_time()
    return catalog, delta_time(start_time, end_time)

# Funciones de consulta sobre el catálogo


def req_1(catalog,product):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    orders = catalog["orders"]
    total= lt.size(orders)
    count=0
    sum_price=0
    min_price=None
    max_price=None
    sum_discount=0
    min_discount=None
    max_discount=None
    sum_boxes=0
    min_boxes=None
    max_boxes=None
    sum_marketing=0
    min_marketing=None
    max_marketing=None
    years={}
    max_amount_order=None
    min_amount_order=None
    for i in range(total):
        order= lt.get_element(orders,i)
        if order["product_name"]!=product:
            continue
        count+=1
        price=float(order["Price_per_box"])
        discount=float(order["Discount_pct"])
        
    
    
    
    


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


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
