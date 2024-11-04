import streamlit  as st
import pandas as pd
import plotly.express as px
from tools.read import eventos
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

st.markdown("## **Seguimiento de los Programas 📆**")



st.html("<br>")

fechas_corte = ['30 de Septiembre']
selected_date = st.sidebar.selectbox("Fecha de corte",fechas_corte)

st.html("<br>")

st.markdown("### **Eventos y Capacitación**")
st.html("<br>")

col1, col4 = st.columns(2)


option_1 = list(eventos.Programa.unique())
option_2 = list(eventos['Región de atención'].unique())

programa=col1.multiselect('**Nombre del Programa**',option_1,placeholder='Todas las opciones')

region=col4.multiselect('**Región**',option_2,placeholder='Todas las opciones')
st.html("<br>")
filtros = []

# Verificar si se ha seleccionado algo en cada multiselect y añadirlo al query
if programa:
    filtros.append(f"Programa in {programa}")
if region:
    filtros.append(f"`Región de atención` in {region}")

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

set_list = ["Set A", "Set B", "SetC"]
df = pd.DataFrame(
    np.random.randint(0, 2, size=(10_000, len(set_list))), columns=set_list
)
fig = plot_upset(
    dataframes=[df],
    legendgroups=["Group X"],
    marker_size=16,
)
df
st.plotly_chart(fig,on_select='rerun')



st.markdown("### **Visitas a Parcelas**")
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