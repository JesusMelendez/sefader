import pandas as pd

path_nov = output_file_name = './data/impacto_nov.csv'

target_cols = {'nombre_tec':'category',
 'NomUsuario':'category',
 'Tipo de bitácora':'category',
 'Ciclo':'category',
 'Régimen hídrico':'category',
 'Tipo de superficie':'category',
 'Cultivo':'category',
 'Costo semilla':'float32',
 'Análisis de suelo':'float32',
 'Análisis de agua':'float32',
 'Nivelación':'float32',
 'Curvas de nivel':'float32',
 'Conservación de suelo y agua':'float32',
 'Aplicación de insumos':'float32',
 'Preparación mecánica del suelo':'float32',
 'Siembra':'float32',
 'Control  físico de malezas':'float32',
 'Riego':'float32',
 'Cosecha manual':'float32',
 'Cosecha motorizada':'float32',
 'Costos comercialización':'float32',
 'Gastos indirectos':'float32',
 'Labores culturales':'float32',
 'Region':'float32',
 'Programa':'category',
 'cumulative_cost_ha':'float32'
 }
columnas = list(target_cols.keys())
df = pd.read_csv(path_nov,usecols=columnas,low_memory=True)

stats = df.groupby('categoria')['valor'].agg(['mean', 'median']).reset_index()