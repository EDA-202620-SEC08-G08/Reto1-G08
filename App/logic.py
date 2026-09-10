import time
import csv
import os

from DataStructures.List import array_list as lt


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    
    catalog={
        "orders": lt.new_list()
    }
    return catalog



# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    start_time = get_time()
    csv.field_size_limit(2147483647)
    path=os.path.join("Data", "Data",filename)
    with open(path, encoding="utf-8-sig") as file:
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
        if order["Product"]!=product:
            continue
        count+=1
        price=float(order["Price_per_Box"])
        discount=float(order["Discount_Pct"])
        boxes=int(order["Boxes_Shipped"])
        marketing=float(order["Marketing_Spend"])
        amount=float(order["Amount"])
        year=order["Order_Date"][:4]
        
        sum_price+=price
        if min_price is None or price <min_price:
            min_price=price
        if max_price is None or price >max_price:
            max_price=price
            
        sum_discount+=discount
        if min_discount is None or discount <min_discount:
            min_discount=discount
        if max_discount is None or discount >max_discount:
            max_discount=discount

        sum_boxes+=boxes
        if min_boxes is None or boxes <min_boxes:
            min_boxes=boxes
        if max_boxes is None or boxes >max_boxes:
            max_boxes=boxes

        sum_marketing+=marketing
        if min_marketing is None or marketing <min_marketing:
            min_marketing=marketing
        if max_marketing is None or marketing >max_marketing:
            max_marketing=marketing

        years[year]=years.get(year,0)+1
        
        if max_amount_order is None:
            max_amount_order= order
        elif amount>float(max_amount_order["Amount"]):
            max_amount_order=order
        elif amount == float(max_amount_order["Amount"]) and marketing < float(max_amount_order["Marketing_Spend"]):
            max_amount_order=order
            
        if min_amount_order is None:
            min_amount_order= order
        elif amount<float(min_amount_order["Amount"]):
            min_amount_order=order
        elif amount == float(min_amount_order["Amount"]) and marketing < float(min_amount_order["Marketing_Spend"]):
            min_amount_order=order

    top_year=None
    top_year_count=0
    for y, c in years.items():
        if c>top_year_count:
            top_year=y
            top_year_count=c
    end_time = get_time()
        
    result = {
        "product": product,
        "count": count,
        "avg_price": sum_price/count if count>0 else 0,
        "min_price": min_price,
        "max_price": max_price,
        "avg_discount": sum_discount/count if count>0 else 0,
        "min_discount": min_discount,
        "max_discount": max_discount,
        "avg_boxes": sum_boxes/count if count>0 else 0,
        "min_boxes": min_boxes,
        "max_boxes": max_boxes,
        "avg_marketing": sum_marketing/count if count>0 else 0,
        "min_marketing": min_marketing,
        "max_marketing": max_marketing,
        "years": years,
        "top_year": top_year,
        "top_year_count": top_year_count,
        "max_amount_order": max_amount_order,
        "min_amount_order": min_amount_order,
    }
    return result, delta_time(start_time, end_time)
    
    


def req_2(catalog, min_price, max_price):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()

    orders = catalog["orders"]
    total = lt.size(orders)

    count = 0
    sum_discount = 0
    sum_marketing = 0
    sum_price = 0

    recent_order = None
    min_amount_order = None
    max_amount_order = None

    for i in range(total):
        order = lt.get_element(orders, i)

        price = float(order["Price_per_Box"])

        if price < min_price or price > max_price:
            continue

        count += 1

        discount = float(order["Discount_Pct"])
        marketing = float(order["Marketing_Spend"])
        amount = float(order["Amount"])
        date = order["Order_Date"]

        sum_discount += discount
        sum_marketing += marketing
        sum_price += price

        if recent_order is None:
            recent_order = order

        else:
            recent_date = recent_order["Order_Date"]

            if date > recent_date:
                recent_order = order

            elif date == recent_date:
                if amount > float(recent_order["Amount"]):
                    recent_order = order

        if min_amount_order is None:
            min_amount_order = order

        else:
            current_min_amount = float(min_amount_order["Amount"])
            current_min_price = float(min_amount_order["Price_per_Box"])

            if amount < current_min_amount:
                min_amount_order = order

            elif amount == current_min_amount:
                if price < current_min_price:
                    min_amount_order = order

        if max_amount_order is None:
            max_amount_order = order

        else:
            current_max_amount = float(max_amount_order["Amount"])
            current_max_price = float(max_amount_order["Price_per_Box"])

            if amount > current_max_amount:
                max_amount_order = order

            elif amount == current_max_amount:
                if price < current_max_price:
                    max_amount_order = order

    if count > 0:
        avg_discount = sum_discount / count
        avg_marketing = sum_marketing / count
        avg_price = sum_price / count
    else:
        avg_discount = 0
        avg_marketing = 0
        avg_price = 0

    end_time = get_time()

    result = {
        "count": count,
        "avg_discount": avg_discount,
        "avg_marketing": avg_marketing,
        "avg_price": avg_price,
        "recent_order": recent_order,
        "min_amount_order": min_amount_order,
        "max_amount_order": max_amount_order
    }

    return result, delta_time(start_time, end_time)

def req_3(catalog, country, channel):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    
    orders = catalog["orders"]
    count = 0
    
    buscar_prod = {}
    buscar_ano = {}
    
    result = {
              "prom_box" : 0,
              "prom_disc" : 0,
              "prom_mark" : 0,
              "prom_box_ship" : 0,
              "prod_frec" : None,
              "ano_frec" : None
              }
    for pos in range(lt.size(orders)):
        orden = lt.get_element(orders, pos)
        
        if country == orden["Country"] and channel == orden["Channel"]:
            count += 1
            
            result["prom_box"] += float(orden["Price_per_Box"])
            result["prom_disc"] += float(orden["Discount_Pct"])
            result["prom_mark"] += float(orden["Marketing_Spend"])
            result["prom_box_ship"] += int(orden["Boxes_Shipped"])
            
            product = orden["Product"]
            year = orden["Order_Date"][:4]
            
            buscar_prod[product] = buscar_prod.get(product, 0) + 1
            buscar_ano[year] = buscar_ano.get(year, 0) + 1
            
    if count == 0:
        return None      
    
    result["prom_box"] = result["prom_box"] / count
    result["prom_disc"] = result["prom_disc"] / count
    result["prom_mark"] = result["prom_mark"] / count
    result["prom_box_ship"] = result["prom_box_ship"] / count
    
    max_count = 0
    
    for llave, valor in buscar_prod.items():
        if valor > max_count:
            max_count = valor
            result["prod_frec"] = llave
    
    max_count = 0
    
    for llave, valor in buscar_ano.items():
            if valor > max_count:
                max_count = valor
                result["ano_frec"] = llave
    
    end_time = get_time()
    time = delta_time(start_time, end_time)
    
    return time, count, result


def req_4(catalog, country, product):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()
    orders = catalog["orders"]
    count = 0
    prom_box = 0
    prom_disc = 0
    prom_mark = 0
    prom_box_ship = 0
    max1 = 0
    max2 = 0
    temp_max = 0
    temp_orden = None
    orden1 = None
    orden2 = None
    amount1 = {}
    amount2 = {}
    for pos in range(0, lt.size(orders)):
        orden = lt.get_element(orders, pos)
        if country == orden["Country"] and product == orden["Product"]:
            count += 1
            prom_box += float(orden["Price_per_Box"])
            prom_disc += float(orden["Discount_Pct"])
            prom_mark += float(orden["Marketing_Spend"])
            prom_box_ship += int(orden["Boxes_Shipped"])
            if float(orden["Amount"]) > max1:
                max2 = max1
                max1 = float(orden["Amount"])
                orden2 = orden1
                orden1 = orden
    
    if count == 0:
        return None      
    
    prom_box = prom_box / count
    prom_disc = prom_disc / count
    prom_mark = prom_mark / count
    prom_box_ship = prom_box_ship / count 

    
    if max1 == max2:
        if float(orden1["Marketing_Spend"]) < float(orden2["Marketing_Spend"]):
            temp_max = max1
            max1 = max2
            max2 = temp_max
            temp_orden = orden1
            orden1 = orden2
            orden2 = temp_orden
        if max1 == max2:
            if int(orden1["Order_ID"][4:]) < int(orden2["Order_ID"][4:]):
                temp_max = max1
                max1 = max2
                max2 = temp_max
                temp_orden = orden1
                orden1 = orden2
                orden2 = temp_orden
            
    
    amount1 = {
            "ID" : orden1["Order_ID"],
            "channel" : orden1["Channel"],
            "date" : orden1["Order_Date"],
            "box_ship" : orden1["Boxes_Shipped"],
            "amount" : max1
            }
    amount2 = {
            "ID" : orden2["Order_ID"],
            "channel" : orden2["Channel"],
            "date" : orden2["Order_Date"],
            "box_ship" : orden2["Boxes_Shipped"],
            "amount" : max2
            }
   
    end_time = get_time()
    time = delta_time(start_time, end_time)
    
    return time, count, prom_box, prom_disc, prom_mark, prom_box_ship, amount1, amount2


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
