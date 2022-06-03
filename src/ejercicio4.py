################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

def suma_lenta(numero, otro_numero):
    """
    Función que suma dos números de manera lenta, sumando de a 1 el segundo valor ingresado.
    """
    suma=numero
    if otro_numero > 0: 
        while otro_numero > 0:
            otro_numero-=1
            suma+=1
    else:
        while otro_numero < 0:
            otro_numero+=1
            suma-=1
    return suma

def principal():
    """
    Funcion que retorna un mensaje declarando la suma de dos números enteros ingresados.
    Precondiciones: Ingreso de números de tipo entero.
    Postcondiciones: Salida del mensaje retornando la suma entre ambos numeros ingresados por el usuario de acuerdo al retorno de la función suma_lenta().
    """
    numero=int(input('Ingrese un número '))
    otro_numero=int(input('Ingrese otro número '))
    suma=suma_lenta(numero, otro_numero)
    print (f'La suma entre {numero} y {otro_numero} es {suma}')
    
if __name__ == "__main__":
    principal()