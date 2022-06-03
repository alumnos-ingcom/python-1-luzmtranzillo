################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Función que prueba que el ingreso y la salida de la función signo(numero)
del ejercicio2.py sean del tipo entero.
"""
import pytest

from src.ejercicio2 import signo


def test_signo():
    """
    Función que testea el tipo de ingreso y salida de la función signo(numero) del
    ejercicio2.py
    """
    numero=1
    resultado_signo=signo(numero)
    assert isinstance(numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(resultado_signo,int),'El retorno de la función signo debe ser de tipo entero'