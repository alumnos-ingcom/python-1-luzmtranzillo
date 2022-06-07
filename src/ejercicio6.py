################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Función que ordena de mayor a menor 3 numeros enteros.En caso de ingresar dos o mas valores iguales,
    la tupla no se realizara y se retornara un mensaje declarando que se han ingresado números iguales.

    """
    resultado_tupla=('')
    if uno > dos and dos > tres:
        resultado_tupla=(uno,dos,tres)
    elif dos > uno and uno > tres:
        resultado_tupla=(dos,uno,tres)
    elif tres > uno and uno > dos:
        resultado_tupla=(tres,uno,dos)
    elif tres > dos and dos > uno:
        resultado_tupla=(tres,dos,uno)
    elif uno > tres and tres > dos:
        resultado_tupla=(uno, tres,dos)
    elif dos > tres and tres > uno:
        resultado_tupla=(dos,tres,uno)
    else:
        resultado_tupla='ha ingresado números iguales'
    return resultado_tupla
    
def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Función que ordena de menor a mayor 3 numeros enteros.En caso de ingresar dos o mas valores iguales,
    la tupla no se realizara y se retornara un mensaje declarando que se han ingresado números iguales.
    """
    resultado_tupla=('')
    if uno < dos and dos < tres:
        resultado_tupla=(uno,dos,tres)
    elif dos < uno and uno < tres:
        resultado_tupla=(dos,uno,tres)
    elif tres < uno and uno < dos:
        resultado_tupla=(tres,uno,dos)
    elif tres < dos and dos < uno:
        resultado_tupla=(tres,dos,uno)
    elif uno < tres and tres < dos:
        resultado_tupla=(uno, tres,dos)
    elif dos < tres and tres < uno:
        resultado_tupla=(dos,tres,uno)
    else:
        resultado_tupla='ha ingresado números iguales'
    return resultado_tupla

def principal():
    """
    Tupla ordenada de mayor a menor y viceversa de 3 números ingresados por el usuario.
    Precondiciones:Ingreso de tres números de tipo entero.
    Postcondiciones: Salida de dos tuplas ordenadas de mayor a menor y viceversa de acuerdo al retorno de
    las funciones ordenar_mayor_a_menor() y ordenar_menor_a_mayor().
    """
    uno=int(input('Ingrese un número entero '))
    dos=int(input('Ingrese un número entero '))
    tres=int(input('Ingrese un número entero '))
    mayor_a_menor=ordenar_mayor_a_menor(uno, dos, tres)
    menor_a_mayor=ordenar_menor_a_mayor(uno, dos, tres)
    print (f'La tupla resultante de números ingresados ordenados de mayor a menor fue: {mayor_a_menor}')
    print (f'La tupla resultante de números ingresados ordenados de menor a mayor fue: {menor_a_mayor}')

if __name__ == "__main__":
    principal()