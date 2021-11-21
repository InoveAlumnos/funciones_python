# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

# Ejemplos de funciones uso
# de la funcion "sorted" de python


def ordenar_menor_mayor(lista_productos):
    precios_ordenados = sorted(lista_productos)
    return precios_ordenados


# --------------------------------
# Aquí dentro definir la función "ordenar_mayor_menor"
# Profesor: Crear una función "ordenar_mayor_menor"
# copiando el fucionamiento de "ordenar_menor_mayor"
# Esta vez utilice el parámetro "reverse" con el valor "True"
# dentro de la función "sorted" para que los resulados
# se ordenen de mayor a menor

# def ordenar_mayor_menor (lista_productos):
def ordenar_mayor_menor(lista_productos):
    precios_ordenados = sorted(lista_productos, reverse=True)
    return precios_ordenados
# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Lista productos comprados (del ejemplo anterior)
    productos = [10, 5, 50, 45]

    # Obtener la lista de precios ordenadas de menor a mayor
    precios_menor_mayor = ordenar_menor_mayor(productos)

    # Imprimir la lista de precios ordenada
    print("Lista de precios ordenada de menor a mayor:")
    print(precios_menor_mayor)

    # *****************************
    #       PROFESOR LIVE CODE
    # *****************************
    # Profesor: Crear una función "ordenar_mayor_menor"
    # copiando el fucionamiento de "ordenar_menor_mayor"
    # Esta vez utilice el parámetro "reverse" con el valor "True"
    # dentro de la función "sorted" para que los resulados
    # se ordenen de mayor a menor

    precio_mayor_menor = ordenar_mayor_menor(productos)
    print("Lista de precios ordenada de mayor a menor:")
    print(precio_mayor_menor)

    print("terminamos")




