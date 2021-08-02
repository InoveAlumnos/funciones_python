# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos de variables globales

# Variable global
# variable definida por fuera del bloque main
version = 'v2.0'


def uso_variables():
    # Variable local que solo existe
    # dentro de esta función
    global version
    author = 'Inove'
    print("Programa escrito por", author, "version", version)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Utilizar la variable global dentro del bloque main
    print("La versión de este programa es", version)

    uso_variables()

    # Veremos como el programa falla porque author no existe
    # fuera de la funcion uso_variables
    print(author)

    



