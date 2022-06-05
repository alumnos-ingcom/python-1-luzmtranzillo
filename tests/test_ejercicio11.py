################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Ejercicio 11
"""
import pytest

from src.ejercicio1 import es_multiplo

def test_es_multiplo():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    numero=10
    multiplo=2
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(multiplo, int), 'Debe ingresar un número de tipo entero.'
    assert numero>0, 'Debe ingresar un valor para número positivo.'
    assert multiplo>0, 'Debe ingresar un valor para multiplo positivo.'
    assert resultado==True, 'La operación se ha realizado de manera incorrecta. La función debiera retornar True.'
    
