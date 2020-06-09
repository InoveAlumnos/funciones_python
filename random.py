import random
azar = []
print('Bien venido')

def lista_aleatorea(inicio, fin, cantidad):
    if inicio <= cantidad and cantidad >= fin:
        azar= random.randrange(inicio, fin, cantidad)
        print(azar)
        return azar
    else:
        print('Datos fuera de rango\n')
        return

    
def obtener():
    inicio = int(input('Ingrese el parametro inicio\n'))
    fin = int(input('Ingrese el parametro fin\n'))
    cantidad = int(input('Ingrese el parametro cantidad\n'))
    azar = lista_aleatorea(inicio, fin, cantidad)
    print(azar)
    
    


if __name__ == '__main__':
    lista_aleatorea()
    obtener()
