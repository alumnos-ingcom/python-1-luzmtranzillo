################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero indicado es Primo.
"""


def es_primo(numero):
    """
    Función que determina si numero es primo o no.
    """
    resultado=''
    if numero>1:
        for n in range(2,numero):
            if (numero % n) == 0:
                resultado=False
        resultado=True
    else:
        resultado=False
    return resultado

def principal():
    """
    Función que pide un número al usuario y usando el retorno de la función es_primo(numero) y envia un mensaje declarando el resultado. 
    Precondiciones: Ingreso de un número de tipo entero.
    Postcondiciones: Salida de un mensaje declarando si el número ingresado es primo o no de acuerdo al retorno de la función es_primo().
    """
    numero=int(input('Ingrese un número '))
    tipo=es_primo(numero)
    if tipo:
        print('El numero ingresado es un número primo')
    else:
        print('El número ingresado no es un número primo')

if __name__ == "__main__":
    principal()
