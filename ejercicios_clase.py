#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import random


def ej1():
    # Ejercicios con funciones del sistema
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle
    https://docs.python.org/3.7/library/functions.html

    La función debe retornar el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado
    '''
    #print(random.sample(numeros, 2))  # probando algunas funciones
    #print(numeros[random.randint(0,6)])
    #print(random.choice(numeros))
    longitud = len(numeros)
    if longitud > 0:
        minimo = min(numeros)
        maximo = max(numeros)
        suma = minimo + maximo
        promedio = suma / 2
        print(promedio)
    elif longitud == 0:
        print('No se puede obtener el promedio de una lista vacia\n')




def ej2():
    # Ejercicios con modulos del sistema
    inicio = 0
    fin = 10

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.
    def lista_aleatoria (inicio, fin, cantidad)

    Dicha función debe retornar la lista de elementos random generados.
    '''

import math  
import random

azar = []
print('Bien venido')
inicio = 0
fin = 0
cantidad = 0
azar = []

def lista_aleatorea(inicio, fin, cantidad):
    i = 0
    while i < cantidad:
            azaroso= random.randrange(inicio, fin, cantidad)
            azar.append(azaroso)
            i += 1
    else:
        return azar

            
def obtener():
    inicio = int(input('Ingrese el parametro inicio\n'))
    fin = int(input('Ingrese el parametro fin\n'))
    rango = fin - inicio
    cantidad = int(input('Ingrese el parametro cantidad\n'))
    if cantidad <= rango and cantidad > 0:
        azar = lista_aleatorea(inicio, fin, cantidad)
        numero_1 = random.choice(azar)
        numero_2 = random.choice(azar)
        print('Numero 1', numero_1)
        print('Numero 2', numero_2)
        raiz_cuadrada_1 = math.sqrt(numero_1)
        raiz_cuadrada_2 = math.sqrt(numero_2)
        print('Raiz cuadrada de', numero_1, 'es', raiz_cuadrada_1)
        print('Raiz cuadrada de', numero_2, 'es', raiz_cuadrada_2)
        print('Lista random', azar)
    else:
        print('Datos fuera de rango\n')

    
    
if __name__ == '__main__':
    lista_aleatorea(inicio, fin, cantidad)
    obtener()

    '''

    # numeros = lista_aleatoria (inicio, fin, cantidad)

    # Imprima en pantalla la lista de elementos generados
    # print(....)

    # Utilice el método random.choice para obtener 2 numeros
    # de la lista de elementos generados
    # numero_1 = random.choice(...)
    # numero_2 = random.choice(...)

    # Importar en este programa/documento el modulo "math"
    # Calcular la raiz cuadrada (square root) de esos
    # dos numeros obtenidos utilizando el método del
    # módulo "math" que crea correspondiente
    # Documentación oficial de math
    # https://docs.python.org/3.7/library/math.html
    # NOTA: Puede buscar en el medio que prefiera la info
    # solicitada

    # raiz_cuadrada_1 = ....
    # raiz_cuadrada_2 = ....
    '''

def ej3():
    # Ejercicios de listas y métodos
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python
    La función no hace falta que retorne la lista ordenada,
    ya que al tratarce de una lista se pasa como referencia
    a la función (es decir que las modificaciones realizadas
    en la función afectan a la variable pasada como argumento)
    '''
    
import math

numeros = []

def ordenar(numeros):
    numeros.sort(reverse=True)
    return numeros


def crear_lista():
    numeros = []
    cuantos = 0
    cuantos = int(input('Cuantos numero desea ordenar\n'))
    i = 0
    while i < cuantos:
        numero = int(input('Ingresar numero\n'))
        numeros.append(numero)
        i += 1
    ordenar(numeros)
    print(numeros)



if __name__ == '__main__':
    ordenar(numeros)
    crear_lista()


def ej4():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado 
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''

def contar():
    i = 0
    numero = 0
    total = 0
    inicio = 1
    fin = 9
    cantidad = 5
    azar = lista_aleatorea(inicio, fin+1, cantidad)
    while i < cantidad:
        numero = azar[i]
        repe = azar.count(numero)
        print('El numero', numero, 'se repite', repe, 'veces')
        total = total + repe
        if total != cantidad:
            i += 1
        else:
            if total == cantidad:
                print(azar)
                break
    else:
        if i == cantidad:
            print(azar)


if __name__ == '__main__':
    lista_aleatorea(inicio, fin, cantidad)
    contar()

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)

def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "buscar",
    que genere una lista con los índice de las posiciones
    en donde se encuentra dicho elemento en la lista.
    Si el elemento en la lista no existe, la función
    debe retornar una lista vacia.
    Para encontrar los índices del elemento en la lista
    puede usar el método "index" o bucles.
    Recuerde que el elemento puede repetirse más de una
    vez en la lista.
    '''

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
