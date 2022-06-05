################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test que testea la función es_multiplo (numero, multiplo) del ejercicio11.py.
"""
import pytest

from src.ejercicio11 import es_multiplo

def test_es_multiplo():
    """
    Función que testea que el tipo de entrada y salida sean del tipo correcto en la función es_multiplo(numero, multiplo) y que las condiciones de ingreso y el retorno sean correctos.
    """
    numero=2
    multiplo=10
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(multiplo, int), 'Debe ingresar un número de tipo entero.'
    assert numero>0, 'Debe ingresar un valor para número positivo.'
    assert multiplo>0, 'Debe ingresar un valor para multiplo positivo.'
    assert resultado==True, 'La operación se ha realizado de manera incorrecta. La función debiera retornar True.'
    
