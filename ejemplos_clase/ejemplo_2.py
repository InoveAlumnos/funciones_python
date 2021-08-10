# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos de llamada a funciones con parámetros

def imprimir_nombre(nombre, apellido):
    nombre_completo = nombre + ' ' + apellido
    print(nombre_completo)


def superficie_circulo(radio):
    resultado = 3.14 * (radio**2)
    return resultado


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Imprimir mi nombre completo
    imprimir_nombre('Inove', 'Escuela')

    # Calcular la superficie de un círculo
    # la función retorna el resultado
    superficie = superficie_circulo(4)
    # superficie es el valor que retorna "superficie_circulo"
    print("Superficie del círculo:", superficie)



