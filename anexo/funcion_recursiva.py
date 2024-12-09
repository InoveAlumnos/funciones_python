# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 1.0

def factorial(numero):
    producto = 1
    if numero > 0:
        producto = numero*factorial(numero-1)
        return producto
    return producto

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numero = int(input("Ingrese número: "))
    resultado = factorial(numero)
    print(resultado)

    print("terminamos")




