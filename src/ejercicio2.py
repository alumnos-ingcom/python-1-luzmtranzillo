################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""

def signo(numero):
    '''
    Función que evalua si el numero ingresado es positivo, negativo o cero.
    '''
    signo=''
    if numero+numero > 0:
        signo=1
    elif numero+numero < 0:
        signo=-1
    else:
        signo=0
    return signo


def principal():
    """
    El usuario ingresa un número y se imprime un mensaje declarando el signo del valor ingresado
    Precondiciones: Ingreso de números de tipo entero.
    Poscondiciones: Salida de un mensaje declarando el signo del numero ingresado.
    """
    numero=int(input('Ingrese un número '))
    signo_numero=signo(numero)
    if signo_numero==1:
        print ('El número ingresado es positivo.')
    elif signo_numero==-1:
        print ('El número ingresado es negativo.')
    else:
        print('El número ingresado es cero')
if __name__ == "__main__":
    principal()