# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos de parámetros ocultos en funciones conocidas

def cantidad_letras(lista_palabras):
    for palabra in lista_palabras:
        cantidad_letras = len(palabra)
        print('Cantidad de letras de {}: {}'.format(palabra, cantidad_letras))


def ordenar_palabras(lista_palabras, operador):
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
        
    print(lista_palabras)


def max_max(lista_palabras):
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
    print('La palabra "te" aparece {} veces'.format(cantidad_max))

    # Buscamos la palabra que más se repite en la lista
    # cambiando el criterio de búsqueda "key" por el función
    # count que se aprovechó antes.
    max_repeticiones = max(lista_palabras, key=lista_palabras.count)
    print('La palabra con más repetición en la lista es "{}"'.format(max_repeticiones))


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    lista_palabras = ['vida', 'te', 'inove', 'dia', 'te']

    # Cuantas letras tiene cada palabra en la lista?
    cantidad_letras(lista_palabras)

    # Ordenar las palabras de mayor a menor por orden alfabético
    ordenar_palabras(lista_palabras, 1)

    # Ordenar las palabras de mayor a menor por cnatidad de letras
    ordenar_palabras(lista_palabras, 2)

    # Ingresar mal el operador
    ordenar_palabras(lista_palabras, 56)

    # Parámetros ocultos por defecto de la función max
    max_max(lista_palabras)

    



