# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

# Ejemplos de funciones integrador

# *****************************
#       PROFESOR LIVE CODE
# *****************************
# Debe copiar de los ejemplos anteriores
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
# Aquí dentro definir la función "calcular_precio_total"
# def calcular_precio_total(lista_productos):
def calcular_precio_total(lista_productos):
    precio_total = sum(lista_productos)
    return precio_total
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
    # cantidad = cantidad_productos....
    cantidad = cantidad_productos()

    # 2) Obtener el precio de cada producto comprado
    # en una lista de "productos"
    # productos = precio_productos(....)
    productos = precio_productos(cantidad)

    # 3) Obtener el precio total de la compra
    # precio_total = calcular_precio_total(....)
    precio_total = calcular_precio_total(productos)

    # 4) Imprimir en pantalla el precio total de la compra
    # print(...)
    print("El precio total de la compra es:", precio_total)

    print("terminamos")




