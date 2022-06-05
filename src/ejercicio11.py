################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""
def es_multiplo(numero, multiplo):
    """
    Funcion que mediante sumas evalua si el valor ingresado es multiplo de número, arrojando un valor de True o False.
    """
    valor_numero=numero
    while valor_numero < multiplo:
        valor_numero+=numero
    if valor_numero==multiplo:
        return True
    else:
        return False

def principal():
    """
    Función que de acuerdo al retorno de la función es_multiplo(numero, multiplo)
    declara si el segundo número ingresado por un usuario es multiplo del primero .
    Precondiciones:Ingreso de dos números de tipo entero.
    Postcondiciones: Salida de un mensaje declarando si el segundo numero ingresado es multiplo del primero.
    """
    numero=int(input('Ingrese un número '))
    multiplo=int(input('Ingrese otro número '))
    resultado=es_multiplo(numero, multiplo)
    if resultado==True:
        print(f'{resultado}: el segundo número ingresado es multiplo del primero.')
    else:
        print(f'{resultado}: el segundo número ingresado no es multiplo del primero.')

if __name__ == "__main__":
    principal()
