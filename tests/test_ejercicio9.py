################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Función que testea la funcion factores_primos(numero) del ejercicio9.py
"""
import pytest

try:
    from ejercicio8 import es_primo
except ImportError: 
    from src.ejercicio8 import es_primo

from src.ejercicio9 import factores_primos
    
def test_factores_primos():
    """
    Función que testea que el tipo de entra y salida sean correctas para la funcion factores_primos(numero), y que su resultado sea el correcto. 
    """
    numero=10
    resultado=factores_primos(numero)
    assert isinstance(numero, int), 'Debe ingresar un número de tipo int.'
    assert isinstance(resultado, tupla), 'La función debe retornar una tupla de números enteros.'
    assert resultado==(2, 5), 'La tupla se ha generado erroneamente.'
    assert numero>1, 'Números menores a 1 no tienen factores primos.'