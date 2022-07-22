import pandas as pd
import requests
import numpy as np


def point_interest(df_fin, ask, num, path='./datasets/results/specific_point_of_interest.csv', theme='Place of Interest'):
    # Función que nos devuelve n resultados en base al theme del usuario.
    # analizar cómo poder elegir el theme haciendo que el sort anterior sea posterior al rename de columnas.
    is_poi = df_fin.loc[:, theme] == ask
    df_poi = df_fin.loc[is_poi]
    df_poi = df_poi.reset_index(drop=True)
    csv_poi = df_poi.head(int(num)).to_csv(path, index=False)
    return print('Se ha generado un archivo csv con la respuesta en la siguiente ruta ./datasets/results/ \n',  df_poi.head(int(num)))

def all_monuments(df_fin, bics, path='./datasets/results/all_points_of_interests.csv', theme='Place of Interest'):
    # función que nos devuelve un listado de n resultados por cada theme indicado por el usuario
    poi_uniques = df_fin[theme].unique().tolist()
    df = df_fin.loc[:, 'Place of Interest'] == 'A Neruda-El Ser alado'
    df1 = df_fin.loc[df]
    df1 = df1.reset_index(drop=True)
    df1 = df1.head(0)
    for i in poi_uniques:
        df_2 = df_fin.loc[:, theme] == i
        df2 = df_fin.loc[df_2]
        df2 = df2.reset_index(drop=True)
        df2 = df2.head(int(bics))
        df1 = df1.append(df2, ignore_index=True)
    csv_full = df1.to_csv(path, index=False)
    return print(df1.head())