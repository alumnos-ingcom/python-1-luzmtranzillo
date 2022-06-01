################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""

def compara(numero, otro_numero):
    """
    Esta función retorna:
    -1 si el primero es menor que el segundo
    0 si son iguales
    1 si el primero es mayor que el segundo
    """
    if numero-otro_numero>0:
        return 1
    elif numero+otro_numero==numero+numero:
        return 0
    else:
        return -1

def principal():
    """
    Comparación de números numeros ingresados, y se declara cual es mayor o sin son iguales.
    """
    numero=int(input('Ingrese un número '))
    otro_numero=int(input('Ingrese otro número '))
    comparacion=compara(numero, otro_numero)
    if comparacion==1:
        print('El primer numero es mayor al segundo')
    elif comparacion==0:
        print('Los numeros ingresados son iguales')
    else:
        print('El primer número es menor al segundo')

if __name__ == "__main__":
    principal()
