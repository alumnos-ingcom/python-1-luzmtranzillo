################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Función que prueba que el ingreso y la salida de la función signo(numero)
del ejercicio2.py sean del tipo entero y string respectivamente. 
"""
import pytest

from src.ejercicio2 import signo


def test_signo_positivo():
    """
    Función que testea  el tipo de ingreso y salida de la función signo(numero) del
    ejercicio2.py sean correctas para los casos positivos.
    """
    numero=1
    resultado_signo=signo(numero)
    assert isinstance(numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(resultado_signo,str),'El retorno de la función signo debe ser de tipo string'
    assert resultado_signo=='positivo', 'El resultado debe declarar el string: positivo'
    
def test_signo_negativo():
    """
    Función que testea  el tipo de ingreso y salida de la función signo(numero) del
    ejercicio2.py sean correctas para los casos negativos.
    """
    numero=-1
    resultado_signo=signo(numero)
    assert isinstance(numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(resultado_signo,str),'El retorno de la función signo debe ser de tipo string'
    assert resultado_signo=='negativo', 'El resultado debe declarar el string: negativo'
    
def test_signo_cero():
    """
    Función que testea  el tipo de ingreso y salida de la función signo(numero) del
    ejercicio2.py sean correctas para los casos en los que el número ingresado sea cero.
    """
    numero=0
    resultado_signo=signo(numero)
    assert isinstance(numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(resultado_signo,str),'El retorno de la función signo debe ser de tipo string'
    assert resultado_signo=='cero', 'El resultado debe declarar el string: cero'