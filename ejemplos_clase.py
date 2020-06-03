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

pi = math.pi


def superficie_circulo(radio):
    return pi * (radio**2)


def incrementar(contador, paso=1):
    contador += paso
    texto = 'Incrementar contador en ' + str(paso)
    print(texto)
    return contador


def contexto():
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
    print('''La superficie de un circulo radio {}
          es {:.2f}'''.format(r, superficie))

    numero = -5
    print('El modulo de {} es {}'.format(numero, abs(numero)))


def modulo():
    # Ejemplo de uso de modulos
    palabras = ['Inove', 'Python', 'escuela', 'codigo']
    it.print_palabras_ordenadas(palabras)

    palabra = palabras.pop()    # Extrae la última palabra
    print('{}: Cantidad letras {}'.format(palabra,
                                          cantidad_letras(palabra)))

    inovetools.print_palabras_ordenadas(palabras)
    palabra = palabras.pop(0)   # Extra la primera palabra, índice = 0
    print('{}: Cantidad letras {}'.format(palabra,
                                          cantidad_letras(palabra)))

    print('Inovetools version,', it.__version__)


def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero, '...', sep='', end='')
        cuenta_regresiva(numero)
    else:
        print('Boom!')
    print('Fin de la recursividad, numero', numero)


def recursivo():
    # Ejemplo de uso de funciones recursivas
    cuenta_regresiva(4)


def max_max():
    # Ejemplo de diferentes formas de utilizar max
    lista = ['vida', 'te', 'Inove', 'dia', 'te']

    # Buscamos la palabra alfabéticamente mayor
    max_alfabeticamente = max(lista)
    print('La palabra alfabéticamente más grande:', max_alfabeticamente)

    # Buscamos la palabra con mayor cantidad de letras
    max_tamaño = max(lista, key=len)
    print('La palabra más larga:', max_tamaño)

    cantidad_max = lista.count('Max')

    # Buscamos la palabra que más se repite
    max_repeticiones = max(lista, key=lista.count)
    print('La palabra con repetición en la lista', max_repeticiones)

    # Una forma de buscar los índices en donde aparecen
    # la palabra más repetida de la lista
    # utilizando el método "index"
    indices = []
    indice_offset = 0
    while True:
        try:
            indice = lista.index(max_repeticiones, indice_offset)
            indice_offset = indice + 1
            indices.append(indice)
        except:
            # Se terminó la lista
            break

    print('Ubicación de la palabra con mayor cantidad de letras:',
          indices)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    contexto()
    modulo()
    recursivo()
    max_max()
