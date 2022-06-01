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
    signo=('')
    if numero+numero > 0:
        signo='positivo'
    elif numero+numero < 0:
        signo='negativo'
    else:
        signo='cero'
    return signo


def principal():
    """
    El usuario ingresa un número y se imprime un mensaje declarando el signo del valor ingresado
    """
    numero=int(input('Ingrese un número '))
    signo_numero=signo(numero)
    print (f'El número ingresado es un número {signo_numero}')

if __name__ == "__main__":
    principal()