# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

# Ejemplos de funciones uso
# de la funcion "sum" de python

def calcular_precio_total(lista_productos):
    precio_total = sum(lista_productos)
    return precio_total


def calcular_precio_total_bucle(lista_productos):
    precio_total = 0
    # Profesor: Implementar un bucle que
    # recorra la variable "lista_productos"
    # y obtener el precio total de la lista

    return precio_total


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Lista productos comprados (del ejemplo anterior)
    productos = [10, 5, 50, 45]

    # Obtener cual es el el precio de productos
    # en la lista
    precio_total_1 = calcular_precio_total(productos)

    # Imprimir el precio total de la lista
    print("Precio total de la lista de producto:", precio_total_1)

    # *****************************
    #       PROFESOR LIVE CODE
    # *****************************
    # Profesor: Implementar lo detallado
    # en la función "calcular_precio_total_bucle"

    # precio_total_2 = calcular_precio_total_bucle(productos)
    # print("Precio total de la lista de producto:", precio_total_2)

    print("terminamos")
