################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Ejercicio4 
"""
import pytest

from src.ejercicio4 import suma_lenta

def test_suma__lenta_numeros_positivo_positivo():
    """
    Esta función verifica los tipos de entrada para la funcion suma_lenta sean de tipo entero y que la operación entre dos números positivos sea correcta.'
    """
    numero=5
    otro_numero=5
    suma=suma_lenta(numero, otro_numero)
    assert isinstance(numero, int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(otro_numero, int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(suma, int), 'El resultado de los números ingresados debe ser de tipo entero'
    assert suma==10 ,'Error:la suma se ha realizado de manera incorrecta'
    
    
def test_suma_lenta_numeros_negativo_negativo():
    """
    Esta función verifica los tipos de entrada para la funcion suma_lenta sean de tipo entero y que la operación entre dos números negativos sea correcta.'
    """
    numero=-5
    otro_numero=-5
    suma=suma_lenta(numero, otro_numero)
    assert isinstance(numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(otro_numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(suma,int), 'El resultado de los números ingresados debe ser de tipo entero'
    assert suma==-10 ,'Error:la suma se ha realizado de manera incorrecta'
    

def test_suma_lenta_numeros_positivo_negativo():
    """
    Esta función verifica los tipos de entrada para la funcion suma_lenta sean de tipo entero y que la operación entre un número positivo y uno negativo sea correcta.'
    """
    numero=5
    otro_numero=-5
    suma=suma_lenta(numero, otro_numero)
    assert isinstance(numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(otro_numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(suma,int), 'El resultado de los números ingresados debe ser de tipo entero'
    assert suma==0 ,'Error:la suma se ha realizado de manera incorrecta'
    

def test_suma_lenta_numeros_lento_negativo_negativo():
    """
    Esta función verifica los tipos de entrada para la funcion suma_lenta sean de tipo entero y que la operación entre un número negativo y uno positivo sea correcta.'
    """
    numero=-5
    otro_numero=5
    suma=suma_lenta(numero, otro_numero)
    assert isinstance(numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(otro_numero,int), 'El número ingresado debe ser de tipo entero'
    assert isinstance(suma,int), 'El resultado de los números ingresados debe ser de tipo entero'
    assert suma==0 ,'Error:la suma se ha realizado de manera incorrecta'
    

def test_suma_lenta_value_error
    except ValueError as exc:
        print('Ha ingresado solo un signo negativo. Debe ingresar un número.')
    

    