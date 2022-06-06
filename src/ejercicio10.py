################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10.Palíndromo.
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo. Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
"""

def remover_caracteres_especiales(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace(",", "")
    cadena = cadena.replace(":", "")
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    return cadena

def es_palindromo(texto):
    """
    Funcion que invierte texto invertido, lo compara con el original y declara si es o no palindromo. 
    """
    inicio=0
    fin=len(texto)-1
    for i in range(0, len(texto)):
        if texto[inicio] == texto[fin]:
            inicio+=1
            fin-=1
            resultado='es un palindromo'
        else:
            resultado='no es un palindromo'
    return resultado



def principal():
    """
    Función que de acuerdo al ingreso de una palabra o frase por el usuario declara si es o no palindromo.
    Precondiciones: Ingreso de una variable de tipo string.
    Postcondiciones: Salida de un mensaje de tipo string declarando si la palabra o frase es palindromo o no.
    """
    cadena=str(input('Ingrese una palabra o frase: '))
    texto=remover_caracteres_especiales(cadena)
    resultado=es_palindromo(texto)
    print(f'El texto ingresado {resultado}.')

if __name__ == "__main__":
    principal()