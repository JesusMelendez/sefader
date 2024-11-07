import streamlit  as st
import pandas as pd
import plotly.express as px
# from tools.read import eventos
import numpy as np
from plotly_upset.plotting import plot_upset

st.set_page_config(layout="wide",page_icon=f'🌽')


# cimmyt = './src/img/cimmyt_new.png'
cl,cl1,cl3,cl4 = st.columns(4)
logo = './src/img/sefader_logo.png'
# cimmyt = './src/img/cimmyt_new.png'
cl.image(logo)
cimmyt_logo = "./src/img/cimmyt.png"
cl4.image(cimmyt_logo)

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

st.markdown("## **Seguimiento de los Programas 📆**")



st.html("<br>")

cortes_ev = {
    '30 de Septiembre': './data/eventos_corte_sept.csv',
    '30 de Octubre': './data/eventos_corte_oct.csv'
}
cols = ['Id_ReporteDeEvento','Municipio donde se realizo el evento','Categoria del evento',
        'Tipo de evento de capacitación','Tipo de evento de comunicacion/difusion','Modalidad del evento',
        'Proyecto','Nombre del reporte','Evento dirigido a','Temas tratados / Tecnologias promovidas',
        'Total de personas capacitadas','Total de organizadores','Emisor del reporte','Bitacora.registrada.por',
        'Programa','Region de atencion','tipo_cap_com']   

innovaciones = {
    '30 de Septiembre': './data/corte_clean_sept_v2.csv',
    '30 de Octubre': './data/corte_clean_oct.csv'
}
cols_inno = ['primary_k','Programa', 'Region de atencion',
 'Agricultura de conservacion','Arreglos de siembra','Comercializacion',
 'Conservacion de agua','Conservacion del suelo','Fertilizacion',
 'Manejo integrado de plagas','Otra','Tecnologias de poscosecha','Variedades mejoradas']

visitas_set = {
    '30 de Septiembre':'./data/visitas_sep_clean.csv',
    '30 de Octubre': './data/visitas_oct_clean.csv'
}
cols_visitas = ['Programa', 'Region de atencion','Id_Parcela','Id_Visitas']

@st.cache_data
def read_data_csv(path : str,cols : list ) ->  pd.DataFrame:
    dataset = pd.read_csv(path,usecols=cols)
    return dataset



 

def app():
    
    fechas_corte = list(cortes_ev.keys())
    selected_date = st.sidebar.radio("Fecha de corte",fechas_corte,index=0)
    

    st.html("<br>")
    
    st.markdown("### **Eventos y Capacitación**")
    st.html("<br>")

    col1, col4 = st.columns(2)

    #read datasets
    eventos = read_data_csv(cortes_ev[selected_date],cols=cols)
    df_inno = read_data_csv(innovaciones[selected_date],cols=cols_inno)
    df_visitas = read_data_csv(visitas_set[selected_date],cols=cols_visitas)
    
    option_1 = list(eventos.Programa.unique())
    option_2 = list(eventos['Region de atencion'].unique())

    programa=col1.multiselect('**Nombre del Programa**',option_1,placeholder='Todas las opciones')

    region=col4.multiselect('**Región**',option_2,placeholder='Todas las opciones')
    st.html("<br>")
    filtros = []

    # Verificar si se ha seleccionado algo en cada multiselect y añadirlo al query
    if programa:
        filtros.append(f"Programa in {programa}")
    if region:
        filtros.append(f"`Region de atencion` in {region}")

    condicion_query = " and ".join(filtros)



    if condicion_query:
        ev_filtrado = eventos.query(condicion_query)
    else:
        ev_filtrado = eventos  


    n_asistentes = int(ev_filtrado['Total de personas capacitadas'].sum())
    n_eventos = ev_filtrado.Id_ReporteDeEvento.nunique()

    cl1, cl3 = st.columns(2)

    cl1.metric("##### Número de asistentes", f"👩‍🌾 {n_asistentes:,d}",delta_color="off")

    cl3.metric("##### Número de eventos",f"📆 {n_eventos:,d}")

        
    fig = px.histogram(ev_filtrado, x="Categoria del evento",height=300)
    st.plotly_chart(fig,on_select='rerun')

    st.html("<br>")

    st.markdown("### **Innovaciones**")
    st.html("<br>")
    
    st.markdown(
    """
    Las siguientes visualizaciones nos ayuda a entender como se implementan las innovaciones, o mejor dicho, los **paquetes tecnológicos**.  A la izquierda 📊, vemos una lista de las innovaciones más frecuentes.
    ⭐ A la derecha, tenemos una gráfica que nos muestra no solo las innovaciones mas frecuentes, sino también qué grupos de innovaciones suelen ir de la mano.
    
    Estos grupos se conectan entre sí a través de una especie de línea punteada , donde cada punto representa una innovación.  ¡Es como un mapa de los distintos paquetes tecnológicos! 

    Gracias a esta herramienta, podemos descubrir patrones de soluciones que no veíamos antes. Por ejemplo, puede que nos demos cuenta en donde se implementa Agricultura de conservación, también suelen implementarse Conservación del suelo, es decir, un paquete tecnológico integral. 
    
    """
    )
    

    
    df_inno.set_index('primary_k',inplace=True)
    if condicion_query:
        df_inno_filtrado = df_inno.query(condicion_query)
        # df_inno_filtrado = df_inno_filtrado[cols_inno[3:]]
        #     # comienza gráfica
        # fig = plot_upset(
        #     dataframes=[df_inno_filtrado],
        #     legendgroups=["Kit técnológico"],
        #     exclude_zeros=True,
        #     sorted_x="d",
        #     sorted_y="a",
        #     row_heights=[0.6, 0.4],
        #     vertical_spacing = 0.,
        #     horizontal_spacing = 0.15)
        # fig.update_layout(
        #     height=700,
        #     width=1800
        # )
        # # fig.show()
        # st.plotly_chart(fig)
    else:
        df_inno_filtrado = df_inno

    df_inno_filtrado = df_inno_filtrado[cols_inno[3:]]
        # comienza gráfica
    fig_2 = plot_upset(
        dataframes=[df_inno_filtrado],
        legendgroups=["Kit técnológico"],
        exclude_zeros=True,
        sorted_x="d",
        sorted_y="a",
        row_heights=[0.6, 0.4],
        vertical_spacing = 0.,
        horizontal_spacing = 0.15)
    fig_2.update_layout(
        height=700,
        width=1800
    )
    
    # renderizar = fig.show()
    # st.html(renderizar)
    st.plotly_chart(fig_2)




    st.markdown("### **Visitas a Parcelas**")
    st.html("<br>")
    
    if condicion_query:
        df_visitas_filtrada = df_visitas.query(condicion_query)
    else:
        df_visitas_filtrada = df_visitas
    
    n_visitas = df_visitas_filtrada['Id_Visitas'].nunique()
   
    st.metric("##### Número de visitas", f"✅ {n_visitas:,d}",delta_color="off")
    # st.metric
    
    fig = px.histogram(df_visitas_filtrada['Id_Parcela'].value_counts().reset_index(),x="count",height=400,labels={'count':'Frecuencia', 'count':'Visitas a Parcelas'})
    st.plotly_chart(fig,on_select='rerun')


app()