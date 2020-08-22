#!/usr/bin/env python
'''
Funciones [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import math

import inovetools as it
import inovetools
from inovetools import cantidad_letras

global_pi = math.pi


def superficie_circulo(radio):
    supercie = global_pi * (radio**2)
    return supercie


def incrementar(contador, paso=1):
    contador += paso
    texto = 'Incrementar contador en ' + str(paso)
    print(texto)
    return contador


def ejemplos_contexto():
    # Ejemplos de funciones y contexto
    contador = 3

    print('Valor contador inicial =', contador)
    incrementar(contador)
    print('Valor contador final =', contador)

    print('Valor contador inicial =', contador)
    contador = incrementar(contador, paso=1)
    print('Valor contador final =', contador)

    r = 2
    superficie = superficie_circulo(radio=r)
    print('La superficie de un circulo radio {} es {:.2f}'.format(r, superficie))

    numero = -5
    print('El modulo de {} es {}'.format(numero, abs(numero)))


def modulo():
    # Ejemplo de uso de modulos
    lista_palabras = ['sol', 'casa', 'nubes']
    lista_palabras.sort()
    it.print_palabras_ordenadas(lista_palabras=lista_palabras)

    print('2)Ordenar alfabéticamente de mayor a menor')
    lista_palabras = ['sol', 'casa', 'nubes']
    inovetools.ordenar_palabras(lista_palabras=lista_palabras)
    inovetools.print_palabras_ordenadas(lista_palabras=lista_palabras)

    print('3)Ordenar cantidad de letras de mayor a menor')
    lista_palabras = ['sol', 'casa', 'nubes']
    it.ordenar_palabras(lista_palabras=lista_palabras, operador=2)
    it.print_palabras_ordenadas(lista_palabras=lista_palabras)

    palabra = lista_palabras.pop(0)   # Extra la primera palabra, índice = 0
    cant_letras_palabra = cantidad_letras(palabra)
    print('{}: Cantidad letras {}'.format(palabra, cant_letras_palabra))

    print('Inovetools version,', it.__version__)


def max_max():
    # Ejemplo de diferentes formas de utilizar max
    palabras = ['vida', 'te', 'Inove', 'dia', 'te']

    # Buscamos la palabra alfabéticamente mayor
    max_alfabeticamente = max(palabras)
    print('La palabra alfabéticamente más grande:', max_alfabeticamente)

    # Buscamos la palabra con mayor cantidad de letras
    max_tamaño = max(palabras, key=len)
    print('La palabra más larga:', max_tamaño)

    cantidad_max = palabras.count('Max')

    # Buscamos la palabra que más se repite
    max_repeticiones = max(palabras, key=palabras.count)
    print('La palabra con repetición en la lista', max_repeticiones)


def hola_mundo():
    print('Hola Mundo!')


def imprimir(mensaje):
    print(mensaje)


def numero_pi():
    num_pi = 3.14159
    return num_pi


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Ejemplos básicos
    # Imprimir hola mundo en pantalla
    hola_mundo()

    # Imprimit un mensaje en pantalla
    imprimir("mensajito")

    # Ejemplo de función con retorno
    # Retorna número pi
    pi = numero_pi()

    ejemplos_contexto()
    modulo()
    max_max()
