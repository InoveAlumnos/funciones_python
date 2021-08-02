# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos de llamada a modulos
# y parámetros por defecto

import math
import random


def superficie_circulo(radio):
    supercie = math.pi * (radio**2)
    return supercie


def numero_aleatorio(inicio, fin):
    numero = random.randrange(inicio, fin+1)
    return numero


def imprimir_nombre(nombre='Max', apellido='Power'):
    nombre_completo = nombre + ' ' + apellido
    print(nombre_completo)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Calcular la superficie de un círculo
    # la función retorna el resultado
    superficie = superficie_circulo(4)
    print("Superficie del círculo:", superficie)

    # Obtener un número aleatorio que se encuentre entre
    # 1 y 6
    print("Numero aleatorio generado", numero_aleatorio(1, 6))

    # Imprimir mi nombre completo
    imprimir_nombre('Inove', 'Escuela')

    # Imprimir mi nombre completo
    imprimir_nombre()

    # Imprimir mi nombre completo
    imprimir_nombre(nombre='Inove')

    # Imprimir mi nombre completo
    imprimir_nombre(apellido='Escuela')

    print("terminamos")
    



