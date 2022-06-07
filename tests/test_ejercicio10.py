################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Función que testea la función es_palindromo(texto) y la función remover_caracteres_especiales(cadena) del ejercicio10.py. 

"""
import pytest

from src.ejercicio10 import es_palindromo, remover_caracteres_especiales

def test_remover_caracteres_especiales():
    '''
    Test que verifica que el tipo de entrafa y salida sea correcto. Además de que el resultado retornado sea correcto.
    '''
    cadena='Oí lo de mamá: me dolió'
    resultado=remover_caracteres_especiales(cadena)
    assert isinstance(cadena, str), 'Debe ingresar una palabra o frase de tipo string.'
    assert isinstance(resultado, str), 'La función debe retornar una palabra o frase de tipo string.'
    assert resultado=='oilodemamamedolio', 'La eliminación de caracteres especiales se ha realizado de manera incorrecta.'
    
    
def test_es_palindromo_true():
    """
    Test que verifica que el tipo de entrada y salida de la funcion es_palindromo(texto) sea correcta. Y que el retorno tambíen lo sea para el caso True. 
    """
    texto='neuquen'
    resultado=es_palindromo(texto)
    assert isinstance(texto, str), 'Debe ingresar una palabra o frase de tipo string.'
    assert isinstance(resultado, str), 'La función debe retornar una palabra o frase de tipo string.'
    assert resultado=='es un palindromo', 'La transformación del texto se ha realizado de manera incorrecta. El texto debiera ser palindromo.'
       
def test_es_palindromo_false():
    """
    Test que verifica que el tipo de entrada y salida de la funcion es_palindromo(texto) sea correcta. Y que el retorno tambíen lo sea para el caso False. 
    """
    texto='reparacion'
    resultado=es_palindromo(texto)
    assert isinstance(texto, str), 'Debe ingresar una palabra o frase de tipo string.'
    assert isinstance(resultado, str), 'La función debe retornar una palabra o frase de tipo string.'
    assert resultado=='no es un palindromo', 'La transformación del texto se ha realizado de manera incorrecta. El texto no debiera ser palindromo.'
