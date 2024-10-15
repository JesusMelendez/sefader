import pandas as pd
from .funciones import read_geojson

global df
path_file = './data/corte_clean_sept.csv'
df = pd.read_csv(path_file,encoding='utf8',usecols=['ID.de.bitacora', 'Tipo.de.superficie', 'ID.del.productor', 'CURP',
       'ID.parcela',  'Estado.areas','Municipio.areas', 'Tipo.de.bitacora', 'Anio.Bitacora', 'Ciclo',
       'Regimen.hidrico', 'Superficie.sembrada','Superficie.Total.de.la.parcela', 'Cultivo.1', 'Cultivo.2', 'Cultivo.3',
        'primary_k', 'Programa', 'type_geometry', 'Region'])

df['Tipo.de.superficie'] = df['Tipo.de.superficie'].astype('category')
df['Anio.Bitacora'] = df['Anio.Bitacora'].astype('category')
df['Region'] = df['Region'].astype('category')
df['Regimen.hidrico'] = df['Regimen.hidrico'].astype('category')
df['Programa'] = df['Programa'].astype('category')


global capa_regiones
capa_regiones = r'./data/regiones_mun_oax.geojson'

global eventos
ev = r'./data/eventos_corte_sept.csv'
eventos = pd.read_csv(ev)