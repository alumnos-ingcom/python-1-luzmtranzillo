################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test de la funciones convertir_a_centigrados y convertir_a_fahrenheit, perteneciente al ejercicio1.py
"""
import pytest

from src.ejercicio1 import convertir_a_centigrados, convertir_a_fahrenheit

def test_convertir_a_centigrados_positivo():
    """
    Esta función verifica que el número ingresado y el resultado de la conversion de la funcion convertir_a_centigrados sea de tipo flotante para grados positivos.
    """
    fahrenheit=32.0
    resultado=convertir_a_centigrados(fahrenheit)
    assert isinstance(fahrenheit,float),"El numero ingresado debe se un numero de tipo flotante"
    assert isinstance(resultado,float),"El resultado debe se un numero de tipo flotante"
    assert resultado==0.0, 'El resultado debe ser un número de tipo float igual a 0.0'
    
def test_convertir_a_centigrados_negativo():
    """
    Esta función verifica que el número ingresado y el resultado de la conversion de la funcion convertir_a_centigrados sea de tipo flotante para grados negativos.
    """
    fahrenheit=-32.0
    resultado=convertir_a_centigrados(fahrenheit)
    assert isinstance(fahrenheit,float),"El numero ingresado debe se un numero de tipo flotante"
    assert isinstance(resultado,float),"El resultado debe se un numero de tipo flotante"
    assert resultado==-35.55555555555556, 'El resultado debe ser un número de tipo float igual a -35.55555555555556'

def test_convertir_a_fahrenheit_positivo():
    """
    Esta función verifica que el número ingresado y el resultado de la conversion de la funcion convertir_a_fahrenit sea de tipo flotante para grados positivos. 
    """
    centigrados=32.0
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(centigrados,float),"El numero ingresado debe se un numero de tipo flotante"
    assert isinstance(resultado,float),"El resultado debe se un numero de tipo flotante"
    assert resultado==89.6, 'El resultado debe ser un número de tipo float igual a 89.6'
    
def test_convertir_a_fahrenheit_negativo():
    """
    Esta función verifica que el número ingresado y el resultado de la conversion de la funcion convertir_a_fahrenit sea de tipo flotante para grados negativos. 
    """
    centigrados=-32.0
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(centigrados,float),"El numero ingresado debe se un numero de tipo flotante"
    assert isinstance(resultado,float),"El resultado debe se un numero de tipo flotante"
    assert resultado==-25.6, 'El resultado debe ser un número de tipo float igual a -25.6'