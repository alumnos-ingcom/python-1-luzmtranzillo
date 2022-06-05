################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Testeo de las funciones sexadecimal_a_decimal(horas, minutos, segundos) y decimal_a_sexadecimal(numero) del ejercicio7.py.
"""
import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

try:
    from ejercicio2 import signo
except ImportError: 
    from src.ejercicio2 import signo 

def test_sexadecimal_a_decimal():
    """
    Función que testea que los ingresos y la salida de la función sexadecimal_a_decimal(horas, minutos, segundos) sea correcta. Además verifica que sus signos sea positivo y el resultado sea correcto.'
    """
    horas=20
    minutos=20
    segundos=20
    resultado=sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(horas, float), 'Debe ingresar un valor de tipo float.'
    assert isinstance(minutos, float), 'Debe ingresar un valor de tipo float.'
    assert isinstance(segundos, float), 'Debe ingresar un valor de tipo float.'
    assert isinstance(resultado, float), 'Debe retornar un valor de tipo float.'
    assert signo(horas)=='positivo', 'Debe ingresar un valor positivo.'
    assert signo(minutos)=='positivo', 'Debe ingresar un valor positivo.'
    assert signo(segundos)=='positivo', 'Debe ingresar un valor positivo.'
    assert resultado==73220 ,'La conversión se ha realizado de manera erronea.'
  
    
def test_decimal_a_sexadecimal():
    """
    Función que testea que el ingreso y la salida de la función decimal_a_sexadecimal(numero) sea correcta. Además verifica que su signo sea positivo y el resultado sea correcto.'
    """
    numero=73220
    resultado=decimal_a_sexadecimal(numero)
    assert isinstance(numero, float), 'Debe ingresar un número de tipo float.'
    assert isinstance(resultado, tuple), 'Debe retornar una tupla con la conversión viceversa de sexadecimal_a_decimal().'
    assert signo(numero)=='positivo', 'Debe ingresar un valor para número positivo.'
    assert resultado==(20, 20, 20), 'La tupla generada es incorrecta.'