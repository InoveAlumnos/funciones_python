#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    print('Comencemos a crear lo nuestro!')

    '''
    Cree un nuevo archivo el cual será su módulo que utilizará
    para resolver todos los ejercicios de está guía.
    En el módulo implemente todas las funciones que le fueron
    solicitadas en "ejercicios_clase":
    - promedio
    - lista_aleatoria
    - ordenar
    - contar
    - buscar

    Importe el módulo a este programa/documento para su uso
    en el resto de los ejercicios
    '''


def ej2():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 con resultados posibles
    de un dado)

    1)
    Utilice la función "ordenar" para ordenar la lista
    de números generados.
    Imprimir en pantalla la lista ordenada

    2)
    Importe el modulo "random" a este programa/documento
    Luego llame al método "shuffle" del módulo "random"
    para volver a mezclar la lista de tiros de dados.

    3)
    Utilice el método "sample" del módulo "random"
    para obtener al hazar 3 valores de la lista
    de números.
    Imprima en pantalla dicha lista de 3 valores.
    '''


def ej3():
    print("Dominando la recursividad")

    '''
    En este ejercicio se deberá plantear el calculo del
    factorial de un número utilizando recursividad
    Primero veamos a que nos referimos con el factorial
    de un número, por ejemplo el factorial (!) de 5 sería:
    --> 5! = 5 * 4 * 3 * 2 * 1
    Mientras que el factorial de 4 sería:
    --> 4! = 4 * 3 * 2 * 1
    Tambíen se podría decir que el factorial de 5 es:
    --> 5! = 5 * 4!
    Es decir, el factorial de 5 (5!) es igual a 5 * factorial de 4 (4!)
    Pueden ver más ejemplos y de que se trata el factorial en el
    siguiente link:
    https://www.disfrutalasmatematicas.com/numeros/factorial.html

    El objetivo es calcular el factorial utilizando recursividad,
    como pueden ver en el ejemplo anterior calcular el factorial de 5
    requiere además calcular el factorial de 4, y calcular el factorial de 4
    requiere calcular el factorial de 3:
    --> 4! = 4 * 3 * 2 * 1
    --> 4! = 4 * 3!
    --> 3! = 3 * 2 * 1
    --> 3! = 3 * 2!

    Les dejamos este ejercicio para que lo piensen, lo pueden dejar para el final
    Cualquier duda nos escriben en el Campus
    '''


def ej4():
    print("Un pequeño paso en la estadística, un gran paso en Python")

    '''
    Lo primero que se solicita es utilizar la función "lista_aleatoria"
    para generar una lista de 20 elementos, en un rango del 0 al 100 inclusive
    A continuación se solicitará que calcule el desvío estandar
    del la lista de números generaods.

    Para calcular el desvió estandar deberá aprovechar la función
    de "promedio", que en estadística al promedio se lo llama "media"
    Deberá calcular la sumatoria de la diferencia de todos los elementos
    de la lista respecto a la "media", dividirlo por la cantidad de elementos
    y calcular la raiz cuadrada.

    Les dejamos una página en donde explica el paso a paso del cálculo
    para que vayan viendo:
    https://es.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step

    El objetivo de este ejercicio es que practiquen la implementación
    matemática de algorítmos.

    Sugerencias:
    1 - Utilizar la función "promedio" para calcular la media
    2 - Para realizar la diferencia entre cada elemento de la lista
        y el promedio utilizar un bucle "for" e ir acumulando el valor
        en una variable "sumatoria".
        Cada valor de diferencia calculada debe aplicarse el módulo "abs"
        (método en math) antes de incorporar dicha diferencia a la variable
        acumulada "sumatoria"
    3 - Utiliza el método "len" para obtener cuantos elementos
        hay en la lista "N".
    4 - Calcular la raiz cuadrada con el método de math correspondiente.

    '''
    # Mi implementación de desvió estandar a continuación:

    '''
    Ahora que han terminado, importe el módulo "statistics" y realice
    los mismos calculos utilizando los metodos del módulo para verificar
    sus resultados
    1 - Utilice el método mean() para contrastar nuestro método "promedio"
    2 - Utilice el método stdev() para contrastar nuestro función desvio_estandar
    '''


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Este ejercicio representa ya un problema que forma parte de un juego
    Lo que se desea realizar es una parte del juego "la generala".

    Deberá realizar una lista para guardar 5 dados, guardar los números
    sacados en esa tirada de de dados (son 5 números del 1 al 6)

    1) El jugador tira la dados y sacar 5 números aleatorios, puede usar
    la función de "lista_aleatoria" para generar dichos números.

    2) Luego debe analizar los 5 números y ver cual es el número que
    más se repitio entre los 5 dados (debe usar la función max con
    la key de list.count)

    3) Una vez reconocido el número más repetido entre los 5, debe
    guardar en una lista aparte con esos números.
    Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4"
    Debe extrarlos de la lista, quedándole dos listas separadas
    dados_guardados = [4,4,4]
    dados_para_tirar= [2,1]
    Utilice el método "pop" para extraer elementos de una lista
    y el método "append" para agregar nuevos.
    Puede utilizar la función creada "buscar" para encontrar
    los índices del número que desea extraer.

    4) Debe volver a tira los dados, generar nuevos
    números aleatorios para aquellos dados reservados para
    tirar (dados_para_tirar). Es decir, que si tengo 2 elementos
    en mi lista de "dados_para_tirar", debo generar dos números
    aleatorios nuevos.
    Otra opción es generar una "lista_generica" nueva y reemplazar
    los "dados_para_tirar".

    5) Luego de tirar nuevamente los datos, por ejemplo digamos
    que salieron los números: 4-1
    Debo volver a quedarme con el "4" ya que es el número que estoy
    buscando.
    Sino salió el "4" vuelvo a tirar todos los dados.
    Si salió un "4" me lo quedo y lo sacó de la lista y lo guardo
    en "dados_guardados".

    5) Debe repetir este proceso hasta que en su lista de "dados
    guardados" tenga "generala", es decir, 5 números iguales.

    '''


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
