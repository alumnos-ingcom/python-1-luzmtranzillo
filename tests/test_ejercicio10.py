################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Función que testea la función es_palindromo(texto) del ejercicio10.py. 

"""
import pytest

from src.ejercicio10 import es_palindromo

def test_es_palindromo():
    """
    Test que verifica que el tipo de entrada y salida de la funcion es_palindromo(texto) sea correcta. Y que el retorno tambíen lo sea. 
    """
    texto=neuquen
    resultado=es_palindromo(texto)
    assert isinstance(texto, str), 'Debe ingresar una palabra o frase de tipo string.'
    assert isinstance(resultado, str), 'La función debe retornar una palabra o frase de tipo string.'
    assert texto==resultado, 'La transformación del texto se ha realizado de manera incorrecta. El texto debiera ser palindromo.'