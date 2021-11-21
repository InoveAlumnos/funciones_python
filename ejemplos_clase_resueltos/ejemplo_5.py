# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

# Ejemplos de funciones integrador

# *****************************
#       PROFESOR LIVE CODE
# *****************************
# Debe copiar de los ejemplos de clase anteriores
# cada unas de las funciones que se detallan

# --------------------------------
# Aquí dentro definir la función "cantidad_productos"
# def cantidad_productos():
def cantidad_productos():
    productos_comprados = int(input("¿Cuántos productos compró?: "))
    return productos_comprados
# --------------------------------

# --------------------------------
# Aquí dentro definir la función "precio_productos"
# def precio_productos(cantidad_productos):
def precio_productos(cantidad_productos):
    productos = []  # lista donde almacenaremos los precios, comienza vacia

    # Realizar un bucle que se ejecute una vez
    # por cada producto comprado, 
    # que permita ingresar el precio por consola
    for i in range(cantidad_productos):
        print("Indique precio del producto", i)
        precio = int(input())
        productos.append(precio)

    # Retornar la lista de precios de productos
    return productos
# --------------------------------

# --------------------------------
# Aquí dentro definir la función "calcular_precio_max"
# def calcular_precio_max(lista_productos):
def calcular_precio_max(lista_productos):
    precio_max = max(lista_productos)
    return precio_max
# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # *****************************
    #       PROFESOR LIVE CODE
    # *****************************
    # Deberá invocar cada una de las funciones
    # que se copiaron de ejemplos anteriores para
    # simular la compra de 4 productos

    # 1) Primero obtener la cantidad de productos comprados
    # cantidad = cantidad_pruductos....
    cantidad = cantidad_productos()

    # 2) Obtener el precio de cada producto comprado
    # en una lista de "productos"
    # productos = precio_productos(....)
    productos = precio_productos(cantidad)

    # 3) Obtener el precio más alto de la lista
    # precio_alto = calcular_precio_max(....)
    precio_alto = calcular_precio_max(productos)

    # 4) Imprimir en pantalla el precio de producto más alto
    # print(...)
    print("El precio más alto ingresado fue:", precio_alto)

    print("terminamos")




