# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

# Ejemplos de llamada a funciones
def imprimir_nombre(nombre, apellido):
    nombre_completo = nombre + ' ' + apellido
    print(nombre_completo)


def cantidad_productos():
    productos_comprados = int(input("¿Cuántos productos compró?: "))
    return productos_comprados


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Imprimir mi nombre completo
    imprimir_nombre('Inove', 'Escuela')

    # Ingresar cuantos productos compró en su compra
    cantidad = cantidad_productos()
    
    # Imprimir la cantidad de productos comprados
    print("Cantidad de productos comprados:", cantidad)

    print("terminamos")



