import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
import numpy as np

url_csv_bic= '../datasets/bicimad_stations.csv' 
dfb = pd.read_csv(url_csv_bic, sep=',') 
df_bic = dfb[['name', 'address', 'geometry.coordinates']]
df_bic[['location.longitude.bic', 'location.latitude.bic']]= df_bic['geometry.coordinates'].str.split(',', expand=True)
df_bic['location.longitude.bic'] = df_bic['location.longitude.bic'].apply(lambda x: float(x[1:]))
df_bic['location.latitude.bic'] = df_bic['location.latitude.bic'].apply(lambda x: float(x[:-1]))
df_bic = df_bic[['name', 'address', 'location.latitude.bic', 'location.longitude.bic']]
endpoint = 'https://datos.madrid.es/egob'
url = '/catalogo/300356-0-monumentos-ciudad-madrid.json'
response = requests.get(endpoint + url)
json_data = response.json()
dfm = pd.DataFrame(pd.json_normalize(json_data['@graph']))
df_monu = dfm[['title', 'address.street-address', 'location.latitude' , 'location.longitude']]
df_monu = df_monu.dropna()
df_bic['key'] = 0
df_monu['key'] = 0
df_pre = df_bic.merge(df_monu, on='key', how='left')
url_df_pre = '../datasets/df.csv'
df_def = pd.read_csv(url_df_pre, sep=',')
zz5 = df_def.sort_values(by = ['title', 'Distancia']).rename(columns={'title':'Place of Interest', 
                                                                      'address.street-address':'Place address',
                                                                     'name':'BiciMAD station',
                                                                      'address':'Station Location'})
zz5['Type of place'] = np.nan
zz5['Type of place'] = zz5['Type of place'].fillna('Monumento de la ciudad de Madrid')
df_final = zz5[['Place of Interest', 'Type of place', 'Place address', 'BiciMAD station', 'Station Location']]
df_final['BiciMAD station'] = df_final['BiciMAD station'].apply(lambda x: x.split('-')[1])
is_poi = df_final.loc[:, 'Place of Interest'] == 'A los Abuelos'
df_poi = df_final.loc[is_poi]
df_poi = df_poi.reset_index(drop=True)
print(df_poi.head(1))
csv_poi = df_poi.head(1).to_csv('../datasets/results/specific_point_of_interest.csv', index=False)
poi_uniques = df_final['Place of Interest'].unique().tolist()
test = df_final.loc[:, 'Place of Interest'] == 'A Neruda-El Ser alado'
test1 = df_final.loc[test]
test1 = test1.reset_index(drop=True)
test1 = test1.head(0)
for i in poi_uniques:
    test_2 = df_final.loc[:, 'Place of Interest'] == i
    test2 = df_final.loc[test_2]
    test2 = test2.reset_index(drop=True)
    test2 = test2.head(1)
    test1 = test1.append(test2, ignore_index=True)
print(test1.head())
csv_full = test1.to_csv('../datasets/results/all_points_of_interests.csv', index=False)