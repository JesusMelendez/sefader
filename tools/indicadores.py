import geopandas as gpd 
import pandas as pd
# from tools.funciones import read_geojson
from utils.con_colors import prYellow
# leer archivos

files = ['./data/poligonos.geojson','./data/poligonos.geojson']

def read_and_join(lista_archivos):
    
    capas = [gpd.GeoDataFrame.from_file(file,crs='EPSG:4326',encoding='utf8') for file in lista_archivos]
    df = pd.concat(capas, ignore_index=True)
    return df
global df_complete
df_complete=read_and_join(files)

prYellow(df_complete.head(2))
# unirlos en pd.DataFrame


# Calcular conteos, sumas, etc

#