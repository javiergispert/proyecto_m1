import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
import numpy as np
from shapely.geometry import Point
import geopandas as gpd

#las dos opciones serían 'mysql' o 'csv' y se podría cambiar el path, query e ip (casa = '92.172.38.71')
def connec_mysql(query="SELECT * FROM bicimad_stations", ip='173.201.189.217', db='/BiciMAD', 
                 root='mysql+pymysql://ironhack_user:', pss='%Vq=c>G5@'): 
    connection_string = root+pss+ip+db
    engine = create_engine(connection_string)
    inspector = inspect(engine)
    df = pd.read_sql_query(query, engine)
    return df

def connec_csv(path):
    # función para únicamente tomar en formato csv la data sin tratar de una conexión a bbdd mysql
    # para nuestro proyecto serían path='./datasets/bicimad_stations.csv' o './datasets/df.csv' (renombrar el archivo a df_merged)
    df = pd.read_csv(path, sep=',')
    return df

def connec_api_mad(endpoint = 'https://datos.madrid.es/egob', url = '/catalogo/300356-0-monumentos-ciudad-madrid.json'):    
    response = requests.get(endpoint + url)
    json_data = response.json()
    df = pd.DataFrame(pd.json_normalize(json_data['@graph']))
    return df