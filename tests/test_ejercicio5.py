################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Testeo de la función division_lenta(dividendo, divisor) del ejercicio5.py
"""
import pytest

from src.ejercicio5 import division_lenta

def test_division_lenta():
    """
    Función que testea el tipo de valor ingresado y saliente de la funcion division lenta(dividendo, divisor). Además de su resultado.
    """
    dividendo=10
    divisor=2
    division=division_lenta(dividendo, divisor)
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(dividendo, tuple), 'El resultado debe ser una tupla con valores de tipo entero.'
    assert division==(5, 0), 'La division se ha realizado de manera incorrecta.'
    
def test_division_lenta_zero():
    '''
    Función que testea con la excepcion ZeroDivisionError los casos de divisor 0.
    '''
    try:
        dividendo=10
        divisor=0
        division=division_lenta(dividendo, divisor)
    except ZeroDivisionError as exc:
        print('No se puede realizar una division con divisor 0')