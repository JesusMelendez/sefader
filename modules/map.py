import pandas as pd
import numpy as np
import re
from shapely.geometry import Point, Polygon
import geopandas as gpd


def to_float(i):
    """
    el parámetro i es un del tipo str
    -----------------------------------
    La función to_float convierte a 'i' a tipo flotante
    -----------------------------------
    devuelve un valor del tipo float
    
    """
    try:
        i = float(i)
    except:
        pass
    return i

def transform(row):
    """
    el parámetro row es un valor del tipo str
    ----------------------------------------------
    separa los elementos de cada row de acuerdo a ciertos caracteres
    depura aquellos que no cumplen ciertas condiciones asignandoles el valor de lista vacia
    transforma cada cadena de texto a valores del tipo float
    ------------------------------------------------
    Retorna coor la cual puede ser una lista con valores flotantes 
    o una lista vacía.

    """
    input = row.split(',')

    size_list = len(input)


    if size_list ==1:
        coor = []
    elif len(input) ==2:
        try:
            pre_punto = map(to_float,input)
            coor=list(pre_punto)
        except ValueError as e:
            print(e)
    elif len(input) >2:
        not_point = re.split(r",0\\n\\n|,0|0\s-|,",row)
        if ("" in not_point):
            not_point.remove("")
            list_with_float = map(to_float,not_point)
            coor = list(list_with_float)
        else:
            list_with_float = map(to_float,not_point)
            coor = list(list_with_float)
        return coor
    
def arreglo(listado):

    ar = listado.sort()
    return ar

def list_sort(lista):
    try:
        arreglo = np.array(lista)
        arr  = arreglo.sort()
    except Error as e:
        print(e)
        
def to_matrix(listado):
    """
    el parámetro listado es un objeto del tipo lista
    -----------------------------------
    transforma una lista a un array de numpy
    asigna la forma del array
    -----------------------------------
    devuelve una matriz
    """
    n = len(listado)
    c = 2
    f =  n/c
    f = int(f)
    vector = np.array(listado)
    matriz = vector.reshape(f,c)
    return matriz

def geometry_apply(x):
    """
    el parámetro x es una lista
    ------------------------------------------
    de acuerdo a la longitud de la lista aplica una o dos funciones
    -----------------------------------------
    devuelve geometry que puede ser un objeto Point, Polygon o un valor None
    """

    n = x

    if len(n) == 2:
        # orden=arreglo(n)
        p=sorted(n)
        geometry = Point(p)
        return geometry
    elif len(n) >5 and len(n) %2 == 0: #Nueva validación
        listado = to_matrix(n)
        geometry = Polygon(listado)
    else:
        geometry = None
    print(geometry)
    return geometry

def typeshape(x):
    """
    El parámetro x es un str
    ----------------------------------------
    De acuerdo al valor genera ciertas cadenas de texto
    ---------------------------------------
    retorna label que es un str
    """
    n=x
    if int(n) == 2:
        label = "Point"
    else:
        label = "Polygon"
    return label    