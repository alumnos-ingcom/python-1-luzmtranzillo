################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""

def division_lenta(dividendo, divisor):
    """
    Funcion que divide un numero de manera lenta, restando de a 1 al dividendo
    """
    cociente=0
    if dividendo>0 and divisor>0: 
        while dividendo>0:
            cociente+=1
            dividendo-=divisor
        resto=dividendo
    elif dividendo<0 and divisor>0:
        while dividendo<0:
            cociente-=1
            dividendo+=divisor
        resto=dividendo
    elif dividendo>0 and divisor<0:
        while dividendo>0:
            cociente-=1
            dividendo+=divisor
        resto=dividendo
    elif dividendo<0 and divisor<0:
        cambio_signo_dividendo=dividendo-(dividendo*2)
        cambio_signo_divisor=divisor-(divisor*2)
        while cambio_signo_dividendo>0:
            cociente+=1
            cambio_signo_dividendo-=cambio_signo_divisor
        resto=cambio_signo_dividendo
    return(cociente, resto)

def principal():
    """
    Funcion que divide un numero ingresado por el usuario por otro de manera lenta y muestra el resultado en pantalla.
    Precondiciones: Ingreso de número de tipo entero.
    Postcondiciones: Salida de un mensaje declarando el cociente y el resto la division entre los dos números ingresados. Ambos resultados son del tipo entero. 
    """
    dividendo=int(input('Ingrese un valor de dividendo '))
    divisor=int(input('Ingrese un valor de divisor  '))
    division=division_lenta(dividendo, divisor)
    cociente=division[0]
    resto=division[1]
    print(f'El resultado de dividir {dividendo} por {divisor} es {cociente} y su resto es {resto}.')
    
if __name__ == "__main__":
    principal()