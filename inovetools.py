#!/usr/bin/env python
'''
InoveTools
---------------------------
Autor: Inove Coding School
Version: 1.2
Descripcion:
Módulo con algunas de las funciones que ejemplifican
las herramientas desarrolladas en este curso.
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

def cantidad_letras(texto):
    return len(texto)


def ordenar_palabras(lista_palabras, operador=1):
    ''' Ordenar palabras alfabeticamente
    o por cantidad de letras de mayor a menor
    '''
    if operador == 1:
        lista_palabras.sort(reverse=True)
    elif operador == 2:
        lista_palabras.sort(reverse=True, key=len)
        # lista_palabras.sort(reverse=True, key=cantidad_letras)
    else:
        print('Operador ingresado', operador, 'incorrecto, ingrese 1 o 2')


def print_palabras_ordenadas(lista_palabras):
    ''' Imprimir palabras ordenadas en pantalla'''
    for i, palabra in enumerate(lista_palabras):
        print(i, ':', palabra, sep='')


if __name__ == "__main__":

    # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    print('\n1)Ordenar utilizando la funcion sort con sus parámetros por defecto',
          end='\n\n')
    lista_palabras = ['sol', 'casa', 'nubes']
    lista_palabras.sort()
    print_palabras_ordenadas(lista_palabras=lista_palabras)

    print('\n2)Ordenar alfabéticamente de mayor a menor', end='\n\n')
    lista_palabras = ['sol', 'casa', 'nubes']
    ordenar_palabras(lista_palabras=lista_palabras)
    print_palabras_ordenadas(lista_palabras=lista_palabras)

    print('\n3)Ordenar cantidad de letras de mayor a menor', end='\n\n')
    lista_palabras = ['sol', 'casa', 'nubes']
    ordenar_palabras(lista_palabras=lista_palabras, operador=2)
    print_palabras_ordenadas(lista_palabras=lista_palabras)
