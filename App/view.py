from DataStructures.List import array_list as lt
import sys
import App.logic as logic

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control


def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    filename=input("Ingrese el nombre del archivo a cargar: ")
    control,time = logic.load_data(control, filename)
    print(f"Datos cargados en {time} milisegundos")
    return control

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    orders = control["orders"]
    for pos in range(lt.size(orders)):
        order = lt.get_element(orders, pos)
        if order["Order_ID"] == id:
            return order
    return None

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    product = input("Ingrese el nombre del producto: ")
    result, time=logic.req_1(control, product)
    print(f"Requerimiento 1 ejecutado en {time} milisegundos")
    print(f"Producto: {result['product']}")
    print(f"Cantidad de ordenes: {result['count']}")
    print(f"Precio promedio: ${result['avg_price']}")
    print(f"Precio mínimo: ${result['min_price']}")
    print(f"Precio máximo: ${result['max_price']}")
    print(f"Descuento promedio: ${result['avg_discount']}")
    print(f"Descuento mínimo: ${result['min_discount']}")
    print(f"Descuento máximo: ${result['max_discount']}")
    print(f"Cantidad de cajas enviadas promedio: {result['avg_boxes']:.2f}")
    print(f"Cantidad de cajas enviadas mínima: {result['min_boxes']}")
    print(f"Cantidad de cajas enviadas máxima: {result['max_boxes']}")
    print(f"Gasto en marketing promedio: ${result['avg_marketing']:.2f}")
    print(f"Gasto en marketing mínimo: ${result['min_marketing']}")
    print(f"Gasto en marketing máximo: ${result['max_marketing']}")
    print(f"Año con mas pedidos: {result['top_year']} ({result['top_year_count']} pedidos)")
    
    max_order = result['max_amount_order']
    print("Pedido de mayor Amount:")
    print(f"  Order_ID: {max_order['Order_ID']}")
    print(f"  Product: {max_order['Product']}")
    print(f"  Country: {max_order['Country']}")
    print(f"  Order_Date: {max_order['Order_Date']}")
    print(f"  Price_per_Box: ${max_order['Price_per_Box']}")
    print(f"  Amount: ${max_order['Amount']}")

    min_order = result['min_amount_order']
    print("Pedido de menor Amount:")
    print(f"  Order_ID: {min_order['Order_ID']}")
    print(f"  Product: {min_order['Product']}")
    print(f"  Country: {min_order['Country']}")
    print(f"  Order_Date: {min_order['Order_Date']}")
    print(f"  Price_per_Box: ${min_order['Price_per_Box']}")
    print(f"  Amount: ${min_order['Amount']}")
    


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    min_price = float(input("Ingrese el precio mínimo por caja: "))
    max_price = float(input("Ingrese el precio máximo por caja: "))

    result, time = logic.req_2(control, min_price, max_price)

    print(f"\nRequerimiento 2 ejecutado en {time:.3f} milisegundos")
    print(f"Cantidad de pedidos encontrados: {result['count']}")

    if result["count"] == 0:
        print("No se encontraron pedidos en ese rango de precio.")
        return

    print(f"Promedio de descuento: {result['avg_discount']:.2f}")
    print(f"Promedio de inversión en marketing: ${result['avg_marketing']:.2f}")
    print(f"Promedio de precio por caja: ${result['avg_price']:.2f}")

    recent_order = result["recent_order"]

    print("\nPedido más reciente:")
    print(f"  Producto: {recent_order['Product']}")
    print(f"  País: {recent_order['Country']}")
    print(f"  Canal: {recent_order['Channel']}")
    print(f"  Fecha: {recent_order['Order_Date']}")
    print(f"  Precio por caja: ${float(recent_order['Price_per_Box']):.2f}")
    print(f"  Monto: ${float(recent_order['Amount']):.2f}")

    min_order = result["min_amount_order"]

    print("\nPedido de menor Amount:")
    print(f"  Producto: {min_order['Product']}")
    print(f"  País: {min_order['Country']}")
    print(f"  Canal: {min_order['Channel']}")
    print(f"  Fecha: {min_order['Order_Date']}")
    print(f"  Precio por caja: ${float(min_order['Price_per_Box']):.2f}")
    print(f"  Monto: ${float(min_order['Amount']):.2f}")

    max_order = result["max_amount_order"]

    print("\nPedido de mayor Amount:")
    print(f"  Producto: {max_order['Product']}")
    print(f"  País: {max_order['Country']}")
    print(f"  Canal: {max_order['Channel']}")
    print(f"  Fecha: {max_order['Order_Date']}")
    print(f"  Precio por caja: ${float(max_order['Price_per_Box']):.2f}")
    print(f"  Monto: ${float(max_order['Amount']):.2f}")


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    country = str(input("Ingrese el pais: "))
    channel = str(input("Ingrese el canal: "))
    if logic.req_3(control, country, channel) != None:
        time, count, result = logic.req_3(control, country, channel)
        print(f"El tiempo requerido fue {time} segundos")
        print(f"Se encontraron {count} pedidos que pasaron el filtro")
        print(f"Promedio precios de cajas: {result['prom_box']}")
        print(f"Promedio gasto marketing: {result['prom_mark']}")
        print(f"Promedio cajas importadas: {result['prom_box_ship']}")
        print(f"Producto mas frecuente: {result['prod_frec']}")
        print(f"Ano mas pedido: {result['ano_frec']}")
    else:
        print(f"No se encontro por el filtro")
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    country = str(input("Ingrese el pais: "))
    product = str(input("Ingrese el producto: "))
    
    resultado = logic.req_4(control, country, product)
    
    if resultado != None:
        time, count, prom_box, prom_disc, prom_mark, prom_box_ship, amount1, amount2 = logic.req_4(control, country, product)
        print(f"El tiempo requerido fue {time} segundos")
        print(f"Se encontraron {count} pedidos que pasaron el filtro")
        print(f"Promedio precios de cajas: {prom_box}")
        print(f"Promedio gasto marketing: {prom_mark}")
        print(f"Promedio cajas importadas: {prom_box_ship}")
        print(f"Amount mas costoso: {amount1}")
        print(f"Segundo amount mas costoso: {amount2}")
    else:
        print(f"No se encontro por el filtro")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    filtro = input("Ingrese MENOR o MAYOR: ").upper()
    product = input("Ingrese el nombre del producto: ")
    start_date = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    end_date = input("Ingrese la fecha final (YYYY-MM-DD): ")

    if filtro != "MENOR" and filtro != "MAYOR":
        print("El filtro debe ser MENOR o MAYOR.")
        return

    result, time = logic.req_5(
        control,
        filtro,
        product,
        start_date,
        end_date
    )

    print(f"\nRequerimiento 5 ejecutado en {time:.3f} milisegundos")
    print(f"Filtro utilizado: {result['filter']}")
    print(f"Cantidad de pedidos encontrados: {result['count']}")

    if result["count"] == 0:
        print("No se encontraron pedidos con ese producto en el rango de fechas.")
        return

    print(f"\nPrecio promedio por caja: ${result['avg_price']:.2f}")
    print(f"Promedio de cajas enviadas: {result['avg_boxes']:.2f}")
    print(f"Promedio de inversión en marketing: ${result['avg_marketing']:.2f}")

    order = result["selected_order"]

    print(f"\nPedido seleccionado ({result['filter']} Amount):")
    print(f"  Precio por caja: ${float(order['Price_per_Box']):.2f}")
    print(f"  Cajas enviadas: {order['Boxes_Shipped']}")
    print(f"  Monto: ${float(order['Amount']):.2f}")
    print(f"  Canal: {order['Channel']}")
    print(f"  Fecha: {order['Order_Date']}")
    print(f"  Inversión en marketing: ${float(order['Marketing_Spend']):.2f}")

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    start_date = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    end_date = input("Ingrese la fecha final (YYYY-MM-DD): ")
    result, time = logic.req_6(control, start_date, end_date)

    print(f"\nRequerimiento 6 ejecutado en {time:.2f} milisegundos")
    print(f"Cantidad de pedidos en el rango de fechas: {result['count']}")

    print(f"\nEl canal más usado es: {result['top_channel_name']}, {result['top_channel_count']} pedidos, recaudo total: ${result['top_channel_amount']:.2f}")
    print(f"El canal que más recauda es: {result['top_revenue_name']}, {result['top_revenue_count']} pedidos, recaudo total: ${result['top_revenue_amount']:.2f}")

    for name, data in result['channels'].items():
        print(f"\nCanal: {name}")
        print(f"Cantidad de pedidos: {data['count']}")
        print(f"Precio promedio: ${data['avg_price']:.2f}")
        print(f"Marketing promedio: ${data['avg_marketing']:.2f}")

        max_order = data['max_order']
        print("Pedido más caro:")
        print(f"Order_ID: {max_order['Order_ID']}")
        print(f"Product: {max_order['Product']}")
        print(f"Country: {max_order['Country']}")
        print(f"Order_Date: {max_order['Order_Date']}")
        print(f"Boxes_Shipped: {max_order['Boxes_Shipped']}")
        print(f"Amount: ${float(max_order['Amount']):.2f}")

        min_order = data['min_order']
        print("\nPedido más barato:")
        print(f"Order_ID: {min_order['Order_ID']}")
        print(f"Product: {min_order['Product']}")
        print(f"Country: {min_order['Country']}")
        print(f"Order_Date: {min_order['Order_Date']}")
        print(f"Boxes_Shipped: {min_order['Boxes_Shipped']}")
        print(f"Amount: ${float(min_order['Amount']):.2f}")

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
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
