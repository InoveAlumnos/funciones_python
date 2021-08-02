# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos de llamada a funciones

def ej1():
    # Ejercicios de práctica numérica
    # Las variables n1, n2 y suma solo existen dentro
    # de esta función "eje1"
    n1 = 5
    n2 = -2.5
    suma = n1 + n2
    print("La suma de {} y {} es {}".format(n1, n2, suma))


def ej2():
    print("Ejercicios de strings")
    # Las variables t1 y t2 solo existen dentro
    # de esta función "eje2"
    t1 = 'Hola'
    t2 = 'Mundo'
    print(t1, t2)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
