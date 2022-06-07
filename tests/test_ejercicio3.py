################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test de la funcionesn compara(numero, otro_numero) perteneciente al ejercicio1.py
"""
import pytest

from src.ejercicio3 import compara


def test_compara_mayor_menor():
    """
    Esta función verifica que los valores ingresados y la salida sean del tipo correcto. Además que verifica que el retorno
    de la función sea correcto. 
    """
    numero=4
    otro_numero=2
    comparacion=compara(numero, otro_numero)
    assert isinstance(numero,int), 'Debe ingresar números de tipo entero'
    assert isinstance(otro_numero,int), 'Debe ingresar números de tipo entero.'
    assert isinstance(comparacion,int), 'La salida de la función debe ser de tipo entero'
    assert comparacion==1, 'Error: La comparación de números ingresados se ha realizado de manera incorrecta. El primer numero es mayor al segundo.'

def test_compara_menor_mayor():
    """
    Esta función verifica que los valores ingresados y la salida sean del tipo correcto. Además que verifica que el retorno
    de la función sea correcto. 
    """
    numero=2
    otro_numero=4
    comparacion=compara(numero, otro_numero)
    assert isinstance(numero,int), 'Debe ingresar números de tipo entero'
    assert isinstance(otro_numero,int), 'Debe ingresar números de tipo entero.'
    assert isinstance(comparacion,int), 'La salida de la función debe ser de tipo entero'
    assert comparacion==-1, 'Error: La comparación de números ingresados se ha realizado de manera incorrecta. El primer numero es menor al segundo.'
    
def test_compara_iguales():
    """
    Esta función verifica que los valores ingresados y la salida sean del tipo correcto. Además que verifica que el retorno
    de la función sea correcto. 
    """
    numero=2
    otro_numero=2
    comparacion=compara(numero, otro_numero)
    assert isinstance(numero,int), 'Debe ingresar números de tipo entero'
    assert isinstance(otro_numero,int), 'Debe ingresar números de tipo entero.'
    assert isinstance(comparacion,int), 'La salida de la función debe ser de tipo entero'
    assert comparacion==0, 'Error: La comparación de números ingresados se ha realizado de manera incorrecta. Los números son iguales.'

