import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
import numpy as np
from shapely.geometry import Point
import geopandas as gpd
import argparse

from modules import macquisition as mac
from modules import mmanipulaciondf as mma
from modules import moperacionaritmetica as mop
from modules import geo_calculations as geo
from modules import mexportar as mex
from modules import mreporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Aplicación estaciones de bicis para Monumentos de la Ciudad de Madrid')
    help_message = 'Tienes dos opciones. Opción 1: "all" obtienes de cada punto de interés tantas estaciones como se soliciten. Opción 2: "one" obtienes de un único punto de interés tantas estaciones como se soliciten'
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    dfb = mac.connec_csv('./datasets/bicimad_stations.csv')
    df_bic = mma.selec_cols(dfb)
    df_bic = mma.dividir_col(df_bic)
    df_bic = mma.float_slicing(df_bic, col='location.longitude.bic', pos1=1)
    df_bic = mma.float_slicing(df_bic, col='location.latitude.bic', pos2=-1)
    dfm = mac.connec_api_mad()
    df_monu = mma.selec_cols(dfm, cols=['title', 'address.street-address', 'location.latitude' , 'location.longitude'])
    df_monu = mma.drop_na(df_monu) 
    df_pre = mma.merge_df(df_bic, df_monu)
    #df_dist = mop.df_dist(df_pre) # tener cuidada ya que son casi 3 horas para generar el df con todas las distancias.
    #df_dist = mex.save_df_csv(df_dist) # esta línea se activa con la anterior
    df_def = mac.connec_csv('./datasets/df.csv')
    df_def = mma.rename_col(df_def, keys=('title', 'address.street-address', 'name', 'address'), values=('Place of Interest', 'Place address', 'BiciMAD station', 'Station Location'))
    df_def = mma.sort_df(df_def, order=True, head=['Place of Interest', 'Distancia'])
    df_def = mma.newcol_values(df_def)
    df_def = mma.split(df_def)
    df_final = mma.selec_cols(df_def, cols=['Place of Interest', 'Type of place', 'Place address', 'BiciMAD station', 'Station Location'])
    if argument_parser().function == 'one':
        ask = input('¿Qué monumento te interesa?: ')
        num = input('¿Cuántas estaciones cercanas quieres que te muestre?: ')
        df_poi = mre.point_interest(df_final, ask, num)
    elif argument_parser().function == 'all':
        bics = input('¿Cuántas estaciones cercanas quieres por cada Monumento?: ')
        df_pai = mre.all_monuments(df_final, bics)
    else:
        result = 'ERROR....Tienes que elegir una de las dos opciones posibles'