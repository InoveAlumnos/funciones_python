# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

# Ejemplos de funciones con listas, 
# y como invocar módulos de python

import random


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

def precio_productos_aleatorios(valor_min, valor_max, cantidad):
    productos = []  # lista donde almacenaremos los precios, comienza vacia
    
    # Realizar un bucle que genere números aleatorios
    # comprendidos entre el rango especificado
    for i in range(cantidad):        
        precio = random.randint(valor_min, valor_max)
        print("Precio aleatorio del producto", i, "es", precio)
        productos.append(precio)

    # Retornar la lista de precios de productos
    return productos


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Cantidad de productos comprados (del ejemplo anterior)
    cantidad = 3

    # Ingresar los precios de los productos comprados
    precios = precio_productos(cantidad)

    # Imprimir los precios de los productos comprados
    print("Precios de los productos comprados:")
    print(precios)

    # Generar aleatoriamente precios para los productos comprados
    # En este ejemplo se visibiliza que valor se asigna a cada parámetro
    precios_aleatorios = precio_productos_aleatorios(valor_min=10, valor_max=150, cantidad=cantidad)

    # Imprimir los precios de los productos comprados
    print("Precios aleatorios de los productos comprados:")
    print(precios_aleatorios)

    print("terminamos")



