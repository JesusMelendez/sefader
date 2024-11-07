import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
from utils.con_colors import prGreen,prPurple
from tools.read import capa_regiones
# from tools.indicadores import df_complete
import leafmap.foliumap as leafmap


# import leafmap.maplibregl as leafmap
from shapely.geometry import Polygon
from shapely.geometry import Point
import plotly.express as px
import pydeck as pdk


#page
st.set_page_config(layout="wide",page_icon=f'🌽')
logo = './src/img/sefader_logo.png'
# cimmyt = './src/img/cimmyt_new.png'
cl,cl1,cl3,cl4 = st.columns(4)
cl.image(logo)
cimmyt_logo = "./src/img/cimmyt.png"
cl4.image(cimmyt_logo)

st.markdown("## **Cobertura de los Programas 🌎**")

st.markdown(
    """
Aquí podrás explorar la información clave de ambos programas de manera sencilla y accesible. Para facilitar la navegación, hemos incluido opciones de **filtro de datos**, los cuales te permitirán ajustar la visualización de acuerdo con tus intereses o necesidades.

¿Cómo usar los filtros?

- **Fecha de corte**: Puedes seleccionar la fecha deseada desde el menú lateral (sidebar), lo que te permitirá ver la información más relevante para ese periodo.
- **Nombre del Programa**: Elige entre los programas disponibles para centrarte en el que te interese.
- **Ciclo Agronómico**: Filtra los datos por el intervalo de tiempo que prefieras, lo que te ayudará a obtener información específica de una época particular.
- **Región**: Selecciona alguna o algunas de las regiones de Oaxaca.
- **Regimen hídrico**: Selecciona de acuerdo al disponibilidad de agua en la producción.

Con estos filtros, tendrás control sobre la información que quieres ver, haciendo que la consulta sea más personalizada y eficiente.

¡Explora y encuentra la información que necesitas!      
        
        
        
        """)
st.html("<br>")


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


cortes_csv = {
    '30 de Septiembre': './data/corte_clean_sept_v2.csv',
    '30 de Octubre': './data/corte_clean_oct.csv'
}

cols_csv = ['ID.de.bitacora', 'Tipo.de.superficie', 'ID.del.productor', 'CURP',
       'ID.parcela',  'Estado.areas','Municipio.areas', 'Tipo.de.bitacora', 'Anio.Bitacora', 'Ciclo',
       'Regimen.hidrico', 'Superficie.sembrada','Superficie.Total.de.la.parcela', 'Cultivo.1', 'Cultivo.2', 'Cultivo.3',
        'primary_k', 'Programa', 'type_geometry', 'Region de atencion','CLAVE']

@st.cache_data
def read_data_csv(path : str,cols : list ) ->  pd.DataFrame:
    dataset = pd.read_csv(path,usecols=cols)
    return dataset
    


def app():
    #
    
    fechas_corte = list(cortes_csv.keys())
    # selected_date = st.sidebar.selectbox("Fecha de corte",fechas_corte)
    selected_date = st.sidebar.radio("Fecha de corte",fechas_corte,index=0)
    
    df = read_data_csv(cortes_csv[selected_date],cols_csv)
    #esto meterlo enla dfuncin de lectura
    df['Tipo.de.superficie'] = df['Tipo.de.superficie'].astype('category')
    df['Anio.Bitacora'] = df['Anio.Bitacora'].astype('category')
    df['Region de atencion'] = df['Region de atencion'].astype('category')
    df['Regimen.hidrico'] = df['Regimen.hidrico'].astype('category')
    df['Programa'] = df['Programa'].astype('category')
    
    st.markdown(f"#####  Fecha de corte:  :green[**{selected_date}**]")
    st.html("<br>")

    col1, col2, col3, col4 = st.columns(4)

    option_1 =  list(df['Programa'].unique())
    option_2 = list(df['Anio.Bitacora'].unique())
    option_3 = list(df['Region de atencion'].unique())
    option_4 = list(df['Regimen.hidrico'].unique())


    catalogos=[option_1,option_2,option_3,option_4]
    # opciones no deseadas
    # remover= ['']


    # def remove_words_from_all_lists(words_to_remove, list_of_lists):

    #     return [[word for word in sublist if word not in words_to_remove] for sublist in list_of_lists]

    # serie_ = pd.Series(option_2)
    # serie_ = serie_[serie_.notnull()].sort_values()
    # option_2_ = list(serie_)
    
    programa=col1.multiselect('**Nombre del Programa**',catalogos[0],placeholder='Todas las opciones')
    ciclo=col2.multiselect('**Ciclo Agronómico**',catalogos[1],placeholder='Todas las opciones')
    region=col3.multiselect('**Región**',catalogos[2],placeholder='Todas las opciones')
    regimen_h=col4.multiselect('**Regime hidríco**',catalogos[3],placeholder='Todas las opciones')

    # Construcción de las condiciones dinámicas para el query
    filtros = []

    # Verificar si se ha seleccionado algo en cada multiselect y añadirlo al query
    if programa:
        filtros.append(f"Programa in {programa}")
    if ciclo:
        filtros.append(f"`Anio.Bitacora` in {ciclo}")
    if region:
        filtros.append(f"Region de atencion in {region}")
    if regimen_h:
        filtros.append(f"`Regimen.hidrico` in {regimen_h}")

    # Construir el string final para el query uniendo las condiciones con "and"
    condicion_query = " and ".join(filtros)



    if condicion_query:
        df_filtrado = df.query(condicion_query)
    else:
        df_filtrado = df  


    #kpi's
    n_mun=df_filtrado['Municipio.areas'].nunique()
    surface =int(df_filtrado['Superficie.sembrada'].sum())
    farmers =  df_filtrado['ID.del.productor'].nunique()
    n_parcelas = df_filtrado['ID.parcela'].count()

    st.html("<hr>")

    cl1, cl2, cl3, cl4 = st.columns(4)


    cl1.metric("##### Número de productores", f"👨‍🌾 {farmers:,d}",delta_color="off")
    cl2.metric("##### Superficie (ha)", f"⬜ {surface:,d}",delta_color="inverse")
    cl3.metric("##### Número de parcelas",f"🟩 {n_parcelas:,d}")
    cl4.metric("##### Número de Municipios", f"📌 {n_mun:,d}")
    st.html("<br>")
    st.html("<br>")
    st.html("<br>")
    n3_1, n3_2 = st.columns([7,3])

 
    # map
    with n3_1:
        

        agrupado=df_filtrado.groupby('CLAVE')['ID.parcela'].count().reset_index()
        agrupado['CLAVE']=agrupado['CLAVE'].astype(str)
        # st.write(agrupado.head(2))
        regiones = gpd.read_file('./data/regiones_oax.geojson',geometry= 'geometry')
        # regiones['CLAVE'] = regiones['CLAVE'].astype(int)

        # st.write(regiones['CLAVE'].head(2))
        new_gdf = regiones.merge(agrupado, on="CLAVE", how="outer")
        new_gdf = gpd.GeoDataFrame(new_gdf, geometry='geometry')
        
        
        
     
        
        ###############################################################################################################################################
        
        # initial_view_state = pdk.ViewState(
        #     latitude=40,
        #     longitude=-100,
        #     zoom=3,
        #     max_zoom=16,
        #     pitch=60,
        #     bearing=0,
        #     height=450,
        #     width=None,
        # )
        
        # min_value = new_gdf['ID.parcela'].min()
        # max_value = new_gdf['ID.parcela'].max()
    
        # geojson = pdk.Layer(
        # "SolidPolygonLayer",
        # data=new_gdf,
        # pickable=True,
        # opacity=0.5,
        # stroked=True,
        # filled=True,
        # extruded=True,
        # wireframe=True,
        # # get_elevation='ID.parcela',
        # # elevation_scale=elev_scale,
        # # get_fill_color="color",
        # # get_fill_color=color_exp,
        # get_line_color=[0, 0, 0],
        # get_line_width=2,
        # line_width_min_pixels=1,
        # )
        # tooltip = {"text": "Name: {Region}"}
        # layers = [geojson]
        
        # r = pdk.Deck(
        # layers=layers,
        # initial_view_state=initial_view_state,
        # map_style="light",
        # tooltip=tooltip,
        # )
        
        # st.pydeck_chart(r)
        
        
        

        
        ######################################################################################################################
        
        m = leafmap.Map(minimap_control=False)
        m.add_tile_layer(
            url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
            name="Google Satellite",
            attribution="Google",
        )


        m.add_geojson(capa_regiones, layer_name="Municipios Oaxaca",zoom_to_layer=True,info_mode=None)
        m.add_geojson('./data/regiones_oax.geojson',layer_name='Regiones Oaxaca',zoom_to_layer=True,info_mode=None)

        
        path_point = r'./data/puntos_sept.geojson'
        path_pol = r'./data/poligonos_sept.geojson'
        cols=['Region','Programa','Anio.Bitacora','Tipo.de.bitacora',
        'Ciclo',
        'Regimen.hidrico',
        'Cultivo.1',
        'Cultivo.2',
        'Cultivo.3',
        'Superficie.sembrada',
        'geometry'
        ]
        # gdf = gpd.GeoDataFrame.from_features(path_point['features'])
        @st.cache_data()
        def read_geoinfo(path):
            gdf = gpd.GeoDataFrame.from_file(path,encoding='utf8',columns=cols)
            return gdf
        #se quito el crs

        puntos = read_geoinfo(path_point)


        # @st.cache_data()
        def lat_long(df):
            df[['Latitude','Longitude']] = df['geometry'].apply(lambda punto: pd.Series([punto.y, punto.x]))
            return df
        puntos = lat_long(puntos)
        
        # colores = {
        #     'AI simplificada':'blue', 'MODULO': 'green', 'AE': 'yellow', 'AI':'red'
        # }
        # Agrega más categorías y colores según sea necesario


        pols = read_geoinfo(path_pol)
        # geojson_color = st.sidebar.color_picker("Selecciona el color para la capa Polígonos", "#00ff00") 
        # pols['color'] = pols['Tipo.de.bitacora'].map(colores)
        
        style = {
            'fillColor': '#00ff00',
            'color': '#00ff00',
            'weight': 1,
            'fillOpacity': 0.6,
        }
        # style={'fillColor': 'color', 'color': '#444444', 'weight': 1, 'opacity': 0.5, 'fillOpacity': 0.5}



        if condicion_query:
            pt_filtrado = puntos.query(condicion_query)
        else:
            pt_filtrado = puntos  # Si no hay filtros seleccionados, mostrar todo el DataFrame    
        if condicion_query:
            pol_filtrado = pols.query(condicion_query)
        else:
            pol_filtrado = pols  # Si no hay filtros seleccionados, mostrar todo el DataFrame
        

        if len(pol_filtrado) < 1:
        
            pass
        else:
            
            
        # Añadir la capa GeoJSON al mapa con el estilo personalizado
            m.add_gdf(pol_filtrado,style_function=lambda x: style,layer_name='Polígono Parcela',zoom_to_layer=False,info_mode="on_click")

        if len(pt_filtrado) < 1:
            pass
        else:

            m.add_points_from_xy(
                pt_filtrado,
                x='Longitude',
                y='Latitude',
                layer_name='Punto Parcela',
                popup=['Region','Programa','Anio.Bitacora',
        'Ciclo',
        'Regimen.hidrico',
        'Cultivo.1',
        'Cultivo.2',
        'Cultivo.3',
        'Superficie.sembrada'
        ],
                color_column="Tipo.de.bitacora",
                icon_names=["gear"],
                spin=True,
                add_legend=True,
                info_mode="on_click"
            )
            # esto va al final de las capas
        

        m.to_streamlit(height=550)

    # x1,x2 = st.columns(2)
    # def surface_chart(df, col1 col2):
    with n3_2:   
        fig = px.bar(df_filtrado, x="Tipo.de.bitacora", y="Superficie.sembrada",height=600)
        st.plotly_chart(fig,on_select='rerun')


app()