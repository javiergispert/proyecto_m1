import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
import numpy as np
from shapely.geometry import Point
import geopandas as gpd

def save_df_csv(df_pre_mer, path='./datasets/df_merged.csv'): #ver si crear una carpeta donde guardar esta data
    # función que convierte un df en csv
    data = df_pre_mer.to_csv(path, index=False)
    return data