
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

def contar():
    inicio = 1
    fin = 9
    rango = fin - inicio
    cantidad = 5
    azar = lista_aleatorea(inicio, fin, cantidad)
    repe = azar.count()
    print(azar)


if __name__ == '__main__':
    lista_aleatorea(inicio, fin, cantidad)
    #obtener()
    contar()
