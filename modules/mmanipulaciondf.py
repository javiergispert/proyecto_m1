import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
import numpy as np
from shapely.geometry import Point
import geopandas as gpd

def selec_cols(df, cols=['name', 'address', 'geometry.coordinates']):
    # realiza un slicing sobre un df en base a las colummnas
    # para nuestro proyecto cols=['name', 'address', 'geometry.coordinates'] o 
    # cols=['title', 'address.street-address', 'location.latitude' , 'location.longitude']
    # cols=['Place of Interest', 'Type of place', 'Place address', 'BiciMAD station', 'Station Location']
    df = df[cols]
    return df

def dividir_col(df, create_cols=['location.longitude.bic', 'location.latitude.bic'], div_col='geometry.coordinates', s=','):
    # función que reparte en dos columnas la data una columna que contiene listas de dos elementos convirtiéndolos en strings
    df[create_cols]= df[div_col].str.split(s, expand=True)
    return df

def float_slicing(df, col, pos1=None, pos2=None):
    # convierte string en float pudiendo hacer un slicing del elemento en esa posición.
    # para nuestro proyecto tendríamos col='location.longitude.bic' o col='location.latitude.bic' y pos1=1 o pos2=-1
    df[col] = df[col].apply(lambda x: float(x[pos1:pos2]))
    return df

def drop_na(df):
    # función para eliminar todas las filas que contengan valores NaN
    df = df.dropna()
    return df

def sort_df (df, order, head=['Place of interest', 'Distancia']):
    # función para ordenar un df en base a columnas y de manera ascendente o descendente con True o False en order.
    df = df.sort_values(by = head, ascending = order)
    return df

def rename_col (df, keys, values):
    # función que renombra tanta columnas como queramos siempre que el número de keys y values coincida
    # para nuestro proyecto sería dict_from_list = {'title':'Place of Interest', 'address.street-address':'Place address',
                                                    #'name':'BiciMAD station','address':'Station Location'}
    key_list = list(keys)
    value_list = list(values)
    dict_from_list = dict(zip(key_list, value_list))
    df = df.rename(columns=dict_from_list)
    return df

def newcol_values(df, new_col='Type of place', fill='Monumento de la ciudad de Madrid'):
    # función que crea una nueva columna a la que se le asigna el mismo valor a todas las filas.
    df[new_col] = np.nan
    df[new_col] = df[new_col].fillna(fill)
    return df

def split(df, col='BiciMAD station', sp='-', pos=1):
    # función para realizar limpieza en un string de los valores de una columna, haciendo un split y slicing a guardar
    df[col] = df[col].apply(lambda x: x.split(sp)[pos])
    return df

def merge_df(df_bic_an, df_monu_an, col='key'):
    # función que crea una columan key con valores 0 en dos dataframes para poder realizar un merge
    df_bic_an[col] = 0
    df_monu_an[col] = 0
    df = df_bic_an.merge(df_monu_an, on=col, how='left')
    return df