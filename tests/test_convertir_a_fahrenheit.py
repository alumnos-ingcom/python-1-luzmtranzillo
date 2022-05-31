################
# Nombre - @luzmtranzillo 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test de la funcion convertir_a_fahrenheit, perteneciente al ejercicio1.py
"""
import pytest

from src.ejercicio1 import convertir_a_fahrenheit

def test_convertir_a_fahrenheit(centigrados):
    """
    Esta función verifica que el numero ingresado y el resultado de la conversion de la funcion convertir_a_fahrenit sea de tipo flotante. 
    """
    centigrados=32
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(centigrados,float),"El numero ingresado debe se un numero de tipo flotante"
    assert isinstance(resultado,float),"El resultado debe se un numero de tipo flotante"
  
