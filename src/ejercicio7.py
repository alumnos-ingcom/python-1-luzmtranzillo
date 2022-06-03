################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado en grados,
minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario,
devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""
def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Función que convierte horas, minutos y segundos a segundos.
    """
    numero=(((horas*60)*60)+(minutos*60)+segundos)
    return numero
    
def decimal_a_sexadecimal(numero):
    """
    Función que convierte un numero a segundos, minutos y horas. 
    """
    calculo_seg = (numero) % 60
    calculo_min = ((numero) // 60) % 60
    calculo_grado = ((numero) // 60) // 60
    return(calculo_seg, calculo_min, calculo_grado)


def principal():
    """
    Función que pide al usuario que ingrese una cantidad de horas, minutos y segundos para convertirlos a segundos
    usando el retorno de la función sexadecimal_a_decimal(horas, minutos, segundos), y la función decimal_a_sexadecimal(numero)
    para retornar una tupla con la conversión en sentido contrario.
    Precondiciones: Ingreso de números de tipo entero.
    Postcondiciones: Salida mensaje declarando los valores retornados de tipo entero. 
    """
    horas=int(input('Ingrese una cantidad de horas '))
    minutos=int(input('Ingrese una cantidad de minutos '))
    segundos=int(input('Ingrese una cantidad de segundos '))
    numero=sexadecimal_a_decimal(horas, minutos, segundos)
    tupla_sexadecimal=decimal_a_sexadecimal(numero)
    print (f'Las horas, minutos y segundos ingresados son {numero} segundos, y la tupla en sentido contrario es {tupla_sexadecimal} siendo en orden de izquierda a derecha segundos, minutos y horas.')

if __name__ == "__main__":
    principal()