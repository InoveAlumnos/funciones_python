# CODE:30
# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# Objetivo:
# Completar el funcionamiento de la función "promedio", evitar
# que el sistema explote si la lista de numeros entregada es vacia

def promedio(numeros):
    print("Funcion promedio")
    resultado = 0
    # La función promedio recibe como parámetro una
    # lista de números. Con ella calcule el promedio como:

    # promedio = sumatoria_numeros / cantidad_numeros

    # Resuelva la sumatoria y la cantidad con las herramientas
    # que desee, recomendamos usar las funciones disponibles
    # de Python para ello:    
    # sum --> obtener la sumatoria de números
    # len --> obtener la cantidad de números

    # La función debe retornar (return) el promedio calculado
    # La función debe contemplar si se le pasa una lista vacia
    # (es decir, de "0" elementos), en ese caso se debe
    # retornar como promedio 0 y evitar que explote el programa

    return resultado


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numeros = [2, 4, 6, 8, 10, 12]

    # Alumno:
    # Llamar a la función en este lugar y capturar el valor del retorno
    # en una variable llamada resultado_promedio
    resultado_promedio = promedio(numeros)

    # Luego imprimir en pantalla el valor resultante:
    # print(....)

    print("terminamos")