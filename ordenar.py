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
