# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos de parámetros ocultos en funciones conocidas


def max_con_palabras(lista_palabras):
    # Ejemplo de diferentes formas de utilizar max

    # Buscamos la palabra alfabéticamente mayor
    max_alfabeticamente = max(lista_palabras)
    print('La palabra alfabéticamente más grande:', max_alfabeticamente)

    # Buscamos la palabra con mayor cantidad de letras
    # Para eso cambiamos el criterio de búsqueda "key"
    # por búsqueda por cantidad de letras "len"
    max_tamaño = max(lista_palabras, key=len)
    print('La palabra más larga:', max_tamaño)

    # Con count podemos contar cuantas veces
    # aparece "te" en la lista de palabras
    cantidad_max = lista_palabras.count('te')
    print(f'La palabra "te" aparece {cantidad_max} veces')

    # Buscamos la palabra que más se repite en la lista
    # cambiando el criterio de búsqueda "key" por el función
    # count que se aprovechó antes.
    max_repeticiones = max(lista_palabras, key=lista_palabras.count)
    print(f'La palabra con más repetición en la lista es {max_repeticiones}')


def max_con_numeros(lista_numeros):
    # Ejemplo de diferentes formas de utilizar max

    # Buscamos la palabra alfabéticamente mayor
    numero_mas_alto = max(lista_numeros)
    print('El número más grande:', numero_mas_alto)

    # Con count podemos contar cuantas veces
    # aparece un número en la lista
    cantidad_de_5 = lista_numeros.count(5)
    print(f'El número "cinco" aparece {cantidad_de_5} veces')

    # Buscamos el número que más veces se repite en la lista
    max_repeticiones = max(lista_numeros, key=lista_numeros.count)
    print(f'El número con más repetición en la lista es {max_repeticiones}')


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    lista_palabras = ['vida', 'te', 'inove', 'dia', 'te']

    # Parámetros ocultos por defecto de la función max
    max_con_palabras(lista_palabras)

    lista_numeros = [1, 3, 3, 5]

    # Parámetros ocultos por defecto de la función max
    max_con_numeros(lista_numeros)

    



