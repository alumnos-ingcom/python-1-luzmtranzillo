################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Testeo de la función division_lenta(dividendo, divisor) del ejercicio5.py
"""
import pytest

from src.ejercicio5 import division_lenta

def test_division_lenta_numeros_positivos():
    """
    Función que testea el tipo de valor ingresado y saliente de la funcion division lenta(dividendo, divisor) sean correctos. Además de su resultado para valores positivos.
    """
    dividendo=10
    divisor=2
    division=division_lenta(dividendo, divisor)
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(division, tuple), 'El resultado debe ser una tupla con valores de tipo entero.'
    assert divisor != 0, 'El divisor debe ser distinto de 0.'
    assert division==(5, 0), 'La division se ha realizado de manera incorrecta.'
    
def test_division_lenta_numeros_negativos():
    """
    Función que testea el tipo de valor ingresado y saliente de la funcion division lenta(dividendo, divisor) sean correctos. Además de su resultado para valores negativos.
    """
    dividendo=-10
    divisor=-2
    division=division_lenta(dividendo, divisor)
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(division, tuple), 'El resultado debe ser una tupla con valores de tipo entero.'
    assert divisor != 0, 'El divisor debe ser distinto de 0.'
    assert division==(5, 0), 'La division se ha realizado de manera incorrecta.'
    
def test_division_lenta_numeros_positivo_negativo():
    """
    Función que testea el tipo de valor ingresado y saliente de la funcion division lenta(dividendo, divisor) sean correctos. Además de su resultado para un dividendo positivo y un divisor negativo.
    """
    dividendo=10
    divisor=-2
    division=division_lenta(dividendo, divisor)
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(division, tuple), 'El resultado debe ser una tupla con valores de tipo entero.'
    assert divisor != 0, 'El divisor debe ser distinto de 0.'
    assert division==(-5, 0), 'La division se ha realizado de manera incorrecta.'
    
def test_division_lenta_numeros_negativo_positivo():
    """
    Función que testea el tipo de valor ingresado y saliente de la funcion division lenta(dividendo, divisor) sean correctos. Además de su resultado para un dividendo negativo y un divisor positivo.
    """
    dividendo=-10
    divisor=2
    division=division_lenta(dividendo, divisor)
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(dividendo, int), 'Debe ingresar un valor de tipo entero'
    assert isinstance(division, tuple), 'El resultado debe ser una tupla con valores de tipo entero.'
    assert divisor != 0, 'El divisor debe ser distinto de 0.'
    assert division==(-5, 0), 'La division se ha realizado de manera incorrecta.'
   
    
