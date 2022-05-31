################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test de la funcion convertir_a_centigrados, perteneciente al ejercicio1.py
"""
import pytest

from src.ejercicio1 import convertir_a_centigrados

def test_convertir_a_centigrados(fahrenheit):
    """
    Esta función verifica que el numero ingresado y el resultado de la conversion de la funcion convertir_a_centigrados sea de tipo flotante.
    """
    fahrenheit=32
    resultado=convertir_a_centigrados(fahrenheit)
    assert isinstance(centigrados,float),"El numero ingresado debe se un numero de tipo flotante"
    assert isinstance(resultado,float),"El resultado debe se un numero de tipo flotante"

