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
        print(azar)
    else:
        print('Datos fuera de rango\n')

    
    


if __name__ == '__main__':
    lista_aleatorea(inicio, fin, cantidad)
    obtener()
