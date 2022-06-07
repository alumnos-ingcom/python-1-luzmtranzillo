################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Función que testea la función es_primo(numero) del ejercicio8.py
"""
import pytest

from src.ejercicio8 import es_primo

def test_es_primo():
    """
    Función que testea el tipo de entrada, el tipo de salida, condiciones de la entrada, y el resultado retornado de la función es_primo(numero).
    """
    numero=2
    resultado=es_primo(numero)
    assert isinstance(numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(resultado, bool), 'El retorno de la función debe ser de tipo booleano.'
    assert resultado==True, 'El resultado esta mal determinado.'
    assert numero>1, 'El número ingresado debe ser mayor a uno.'
