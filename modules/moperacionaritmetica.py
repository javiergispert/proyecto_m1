import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
import numpy as np
from shapely.geometry import Point
import geopandas as gpd

def df_dist(df_pre_mercator, col='Distancia', lata='location.latitude', longa='location.longitude', 
            latb='location.latitude.bic', longb='location.longitude.bic'):
    # función que crea una columna nueva cuyos valores son los resultados de aplicar mercator con la data de 4 columnas.
    df_pre_mercator[col] = df_pre_mercator.apply(lambda x: distance_meters(x[lata], x[longa], x[latb], x[longb]), axis=1)   
    return df_pre_mercator