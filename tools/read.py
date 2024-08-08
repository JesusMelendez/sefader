import pandas as pd
from .funciones import read_geojson

global df
path_file = './data/bitacoras_corte_julio.csv'
df = pd.read_csv(path_file,encoding='utf8')
df = df.iloc[:,0:22]


global capa_regiones
capa_regiones = r'./data/regiones_mun_oax.geojson'
