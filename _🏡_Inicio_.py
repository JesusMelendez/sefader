import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import geopandas as gpd
from utils.con_colors import prGreen,prPurple
from tools.read import df,capa_regiones
# from tools.indicadores import df_complete
import leafmap.foliumap as leafmap
from shapely.geometry import Polygon
from shapely.geometry import Point
import folium
# import folium
#page

st.set_page_config(layout="wide")
# st.title("_Streamlit_ is :red[cool] :sunglasses:")
st.sidebar.markdown('# SEFADER')
fechas_corte = ['30 de Julio']
selected_date = st.sidebar.selectbox("Fecha de corte",fechas_corte)

st.markdown("### Secretaria de Fomento Agroalimentario y Desarrollo Rural")

#kpi's
n_mun=df['Municipio.areas'].nunique()
surface =int(df['Superficie.sembrada'].sum())
union_fields = df['ID.del.productor'] + df['Nombre.Productor'] + df['CURP']
farmers = union_fields.nunique()
col1, col2, col3 = st.columns(3)
col1.metric("Número de Municipios", f"{n_mun:,d}", "100%")
col2.metric("Superficie ", f"{surface:,d}(ha)", "100%")
col3.metric("Número de productores", f"{farmers:,d}", "100%")



# map

st.markdown(f"##### **Al {selected_date}**")

m = leafmap.Map(minimap_control=False)
m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
)

m.add_geojson(capa_regiones, layer_name="Regiones Oaxaca",zoom_to_layer=True,info_mode=None)
m.add_geojson('./data/regiones_oax.geojson',layer_name='Limite Oaxaca',zoom_to_layer=True,info_mode=None)


path_point = r'./data/puntos.geojson'
path_pol = r'./data/poligonos.geojson'
# gdf = gpd.GeoDataFrame.from_features(path_point['features'])
puntos = gpd.GeoDataFrame.from_file(path_point,crs='EPSG:4326',encoding='utf8')
cols=['Anio.Bitacora',
'Ciclo',
'Regimen.hidrico',
'Cultivo.1',
'Cultivo.2',
'Cultivo.3',
'Superficie.sembrada',
'geometry'
]
prGreen(puntos.info())
pols = gpd.GeoDataFrame.from_file(path_pol,crs='EPSG:4326',encoding='utf8')
geojson_color = st.sidebar.color_picker("Selecciona el color para la capa Polígonos", "#00ff00") 
style = {
    'fillColor': geojson_color,
    'color': geojson_color,
    'weight': 1,
    'fillOpacity': 0.6,
}

# Añadir la capa GeoJSON al mapa con el estilo personalizado
m.add_gdf(pols[cols],style_function=lambda x: style,layer_name='Polígono Parcela',zoom_to_layer=False,info_mode="on_click")
# m.add_points_from_xy(
#     new_points,
#     x="longitude",
#     y="latitude",
#     color_column="region",
#     icon_names=["gear", "map", "leaf", "globe"],
#     spin=True,
#     add_legend=True,
# )

m.add_gdf(puntos[cols], style_function=lambda x: style,layer_name='Punto Parcela',zoom_to_layer=False,info_mode="on_click")
# esto va al final de las capas
m.to_streamlit(height=500)
# st_folium(m.to_streamlit(height=500), width=700, height=500)
# prPurple(df_complete.info())

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)