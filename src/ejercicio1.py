################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""

def convertir_a_fahrenheit(centigrados):
    """
    Función que convierte los grados centigrados en grados fahrenheit.
    """
    conversion_fahrenheit=(centigrados*1.8)+32
    return conversion_fahrenheit

def convertir_a_centigrados(fahrenheit):
    """
    Función que convierte los grados fahrenheit en grados centigrados
    """
    conversion_centigrados=(fahrenheit-32)*(5/9)
    return conversion_centigrados


def principal():
    """
    Conversion de grados centigrados a grados fahrenheit ingresados por el usuario y viceversa
    Precondiciones:Valores de tipo float para las variables centigrados y fahrenheit. 
    Poscondiciones: Muestra del mensaje con el resultado de la conversion de grados centigrados y fahrenheit a su viceversa representado en un número de tipo float. 
    
    """
    centigrados=float(input('Ingrese un valor de grados centigrados '))
    fahrenheit=float(input('Ingrese un valor de grado fahrenheit '))
    conversion_fahrenheit=convertir_a_fahrenheit(centigrados)
    conversion_centigrados=convertir_a_centigrados(fahrenheit)
    print (f'Los {centigrados} grados centigrados son {conversion_fahrenheit} grados fahrenheit')
    print (f'Los {fahrenheit} grados fahrenheit son {conversion_centigrados} grados centigrados')

if __name__ == "__main__":
    principal()