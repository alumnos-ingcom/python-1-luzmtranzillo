################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo. Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
"""

def es_palindromo(texto):
    """
    Funcion que invierte texto invertido, lo compara con el original y declara si es o no palindromo. 
    """
    texto_invertido=texto[::-1]
    palindromo=('')
    if texto == texto_invertido:
        palindromo=('es un palindromo')
    else:
        palindromo=('no es un palindromo')
    return palindromo
        
        

def principal():
    """
    Función que de acuerdo al ingreso de una palabra o frase por el usuario declara si es o no palindromo.
    Precondiciones: Ingreso de una variable de tipo string.
    Postcondiciones: Salida de un mensaje de tipo string declarando si la palabra o frase es palindromo o no.
    """
    texto=str(input('Ingrese una palabra o frase: '))
    resultado=es_palindromo(texto)
    print(f'El texto ingresado {resultado}')

if __name__ == "__main__":
    principal()