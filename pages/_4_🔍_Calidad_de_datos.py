import pandas as pd
import numpy 
# from ydata_profiling import ProfileReport
import streamlit as st
import plotly.express as px
# from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide",page_icon=f'🌽')

logo = './src/img/sefader_logo.png'
# cimmyt = './src/img/cimmyt_new.png'
cl,cl1,cl3,cl4 = st.columns(4)
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

st.markdown("## **Calidad de los datos 🔍**")

st.html("<br>")

dataset = {
    'coordenadas': './data/errors_oct_30_.csv',
    'superficie_costo': './data/bitacoras_sup_cost.csv',
    'score':'./data/score_bitacoras.csv'
}

cols_erros=['ID.de.bitacora','Tipo.de.superficie','Bitacora.registrada.por','Coordenadas.areas']
cols_surface =['NomUsuario', 'Hub operativo', 'Superficie Total de la parcela (ha)',
       'ID_Bitacora', 'Tipo de bitacora', 'Año-ciclo-bitacora',
       'Regimen hidrico', 'Id_Cultivos', 'Tipo de superficie',
       'Superficie sembrada (ha)', 'Num_cultivos_registrados',
       'Num_productos_registrados', 'Num_rendimientos_registrados',
       'Costo acumulado']
cols_score = ['NomUsuario', 'Hub operativo', 'Superficie Total de la parcela (ha)',
       'ID_Bitacora', 'Tipo de bitacora', 'Proyecto', 'Anio-ciclo-bitacora',
       'Regimen hidrico', 'Id_Cultivos', 'Tipo de superficie',
       'Porcentaje de avance (por tipo de superficie)']

@st.cache_data
def read_pandas(path, cols,codificacion=None):
    df = pd.read_csv(path, usecols=cols,encoding=codificacion)
    return df

st.markdown(
    """
    En esta sección se muestra los principales situaciones en cuanto a los datos recolectados. En donde se puede listar las principales áreas de oportunidad:
    
    - Ausencia de Valores en variables clave ❓
    - Información que puede salir de la realidad (datos atípicos) ❌
    - Valores en formato distinto al esperado (kg en lugar de ton; por mencionar un caso) ❗

    Lo siguiente es de acuerdo a la **última fecha de corte de información**.
    
    """
)



def app():
    
    
    st.markdown("#### **Conjunto de datos con detalle en coordenadas 🌎**")
    
    errores = read_pandas(dataset['coordenadas'],cols=cols_erros)
    new_names= ['ID Bitacora','Tipo Superficie','Usuario','Coordenadas']
    errores.rename(columns=dict(zip(cols_erros,new_names)),inplace=True)
    st.markdown("""El formato de coordenadas que acepta el sistema es del tipo **decimal**, separado por una coma.
                
                Un ejemplo de coordenadas válidas son: 23.634501, -102.552784 """)
    
    st.write(errores)
    
    
    
    st.markdown("#### **Avance registro de bitácoras 📙**")
    col_1, col_2=st.columns(2)
    with col_1:
        
        st.markdown("#####  **Superficie Costo**")
        st.html("<br>")
        surf_cost = read_pandas(dataset['superficie_costo'],cols=cols_surface,codificacion='1252')
        st.write(surf_cost)
        st.html("<br>")
        st.markdown("#####  **Porcentaje de avance** ")
        st.html("<br>")
        score = read_pandas(dataset['score'],cols=cols_score)
        st.write(score)

    with col_2:
        fig = px.scatter(surf_cost, x="Superficie Total de la parcela (ha)", y="Costo acumulado", marginal_x="histogram", marginal_y="rug")
        st.plotly_chart(fig,on_select='rerun')
        st.html("<br>")
        fig_2 = px.histogram(score,x='Porcentaje de avance (por tipo de superficie)',labels={'x':'Porcentaje de avance (por tipo de superficie)'})
        st.plotly_chart(fig_2,on_select='rerun')

app()


