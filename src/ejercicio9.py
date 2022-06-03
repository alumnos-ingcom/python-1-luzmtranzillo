################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""

from ejercicio8 import es_primo

def factores_primos(numero):
    """
    Función que utiliza la funcion es_primo(numero) del ejercicio 8 para calcular los factores primos de un número. 
    """
    factor = 2
    lista_multiplos= []
    while factor < numero:
        if es_primo(factor) and numero%factor==0:
            lista_multiplos.append(factor)
        factor+=1
    return tuple(lista_multiplos)
    
def principal():
    """
    Función que muestra los valores primos de un numero ingresado, utilizando la función factores_primos(numero).
    Precondiciones:Ingreso de un número de tipo entero.
    Postcondiciones: Salida de un mensaje y una tupla declando los factores primos del número ingresado. 
    """
    numero=int(input('Ingrese un número '))
    resultado_factores=factores_primos(numero)
    print(f'La tupla de factores primos de {numero} es {resultado_factores}')

if __name__ == "__main__":
    principal()