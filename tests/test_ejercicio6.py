################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Test que testea las funciones ordenar_mayor_a_menor(uno, dos, tres) y ordenar_menor_a_mayor(uno, dos, tres) pertenecientes al ejercicio6.py
"""
import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

def test_ordenar_mayor_a_menor_1_2_3():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=3
    dos=2
    tres=1
    tupla=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(3, 2, 1), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_mayor_a_menor_2_1_3():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=2
    dos=3
    tres=1
    tupla=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(3, 2, 1), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_mayor_a_menor_3_1_2():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=2
    dos=1
    tres=3
    tupla=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(3, 2, 1), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_mayor_a_menor_3_2_1():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=1
    dos=2
    tres=3
    tupla=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(3, 2, 1), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_mayor_a_menor_1_3_2():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=3
    dos=1
    tres=2
    tupla=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(3, 2, 1), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_mayor_a_menor_2_3_1():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=1
    dos=3
    tres=2
    tupla=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(3, 2, 1), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_mayor_a_menor_1_1_1():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=1
    dos=1
    tres=1
    tupla=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, str), 'Debe retornar una tupla.'
    assert tupla=='ha ingresado números iguales', 'Los números se han ordenado de manera incorrecta.'

def test_ordenar_menor_a_mayor_1_2_3():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=1
    dos=2
    tres=3
    tupla=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(1, 2, 3), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_menor_a_mayor_2_1_3():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=2
    dos=1
    tres=3
    tupla=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(1, 2, 3), 'Los números se han ordenado de manera incorrecta.'

def test_ordenar_menor_a_mayor_3_1_2():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=2
    dos=3
    tres=1
    tupla=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(1, 2, 3), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_menor_a_mayor_3_2_1():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=3
    dos=2
    tres=1
    tupla=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(1, 2, 3), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_menor_a_mayor_1_3_2():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=1
    dos=3
    tres=2
    tupla=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(1, 2, 3), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_menor_a_mayor_2_3_1():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=1
    dos=3
    tres=2
    tupla=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, tuple), 'Debe retornar una tupla.'
    assert tupla==(1, 2, 3), 'Los números se han ordenado de manera incorrecta.'
    
def test_ordenar_menor_a_mayor_1_1_1():
    """
    Función que verifica que los tipos de entrada y salida sean del tipo correcto, y que la tupla generada sea correcta de acuerdo a los casos planteados.
    """
    uno=1
    dos=1
    tres=1
    tupla=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(uno, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(dos, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tres, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance(tupla, str), 'Debe retornar una tupla.'
    assert tupla=='ha ingresado números iguales', 'Los números se han ordenado de manera incorrecta.'
    