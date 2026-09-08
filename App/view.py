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
    print(f"Datos cargados en {time} segundos")
    return control

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    product = input("Ingrese el nombre del producto: ")
    result, time=logic.req_1(control, product)
    avg_boxes = result['sum_boxes'] / result['count'] if result['count'] > 0 else 0
    avg_marketing = result['sum_marketing'] / result['count'] if result['count'] > 0 else 0
    print(f"Requerimiento 1 ejecutado en {time} segundos")
    print(f"Producto: {result['product']}")
    print(f"Cantidad de ordenes: {result['count']}")
    print(f"Precio promedio: {result['avg_price']}")
    print(f"Precio mínimo: {result['min_price']}")
    print(f"Precio máximo: {result['max_price']}")
    print(f"Descuento promedio: {result['avg_discount']}")
    print(f"Descuento mínimo: {result['min_discount']}")
    print(f"Descuento máximo: {result['max_discount']}")
    print(f"Cantidad de cajas enviadas total: {result['sum_boxes']}")
    print(f"Cantidad de cajas enviadas promedio: {avg_boxes:.2f}")
    print(f"Cantidad de cajas enviadas mínima: {result['min_boxes']}")
    print(f"Cantidad de cajas enviadas máxima: {result['max_boxes'] / result['count']:.2f}")
    print(f"Gasto en marketing total: {result['sum_marketing']:.2f}")
    print(f"Gasto en marketing promedio: {avg_marketing:.2f}")
    print(f"Gasto en marketing mínimo: {result['min_marketing']}")
    print(f"Gasto en marketing máximo: {result['max_marketing']}")
    print(f"Ordenes por año: {result['years']}")
    print(f"Order de mayor valor: {result['max_amount_order']}")
    print(f"Order de menor valor: {result['min_amount_order']}")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


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
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

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

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
