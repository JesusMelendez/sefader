import streamlit  as st
from modules.impacto import df
import plotly.graph_objs as go
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

st.markdown("## **Impacto de los Programas ✅**")

# codigo comentado, en esta parte, los jupyter de costos y costo_rendimiento son el insumo descomentar, y hacer pruebas en local antes de hacer
# un pull en el servidor

# def app():


#     st.markdown("### **Programa de Abasto Seguro de Maíz 🌽**")
    
#     options_ciclo = list(df['Ciclo'].unique())
#     options_cultivo = list(df['Cultivo'].unique())
#     st.selectbox('Ciclo Agronómico',options_ciclo,index=0) 
    
#     col_1, col_2 = st.columns(2)

#     filtros = []
#     if options_ciclo:
#         filtros.append(f"Ciclo in {options_ciclo}")
#     if options_cultivo:
#         filtros.append(f"`Cultivo in {options_cultivo}")
#     condicion_query = " and ".join(filtros)

#     if condicion_query:
#         df = df.query(condicion_query)
#     else:
#         df = df  
    
#     costo = 
#     rendimiento = 

#     col_1.metric("#### Costo Promedio (MXN/ha)"f"{costo}")
#     col_2.metric("#### Rendimiento Promedio (ton/ha)"f"{rendimiento}")
#     with col_1:
#         st.metric("")

     
#     with col_2:
#         st.write('second column')
#         st.write('some content')
    
#     st.markdown("### **Programa de Autosuficiencia Alimentaria 👩‍🌾**")
#     level_2, level_2_2 = st.columns(2)
#     with level_2:
#         st.write('first column')
#         st.write('some content')
        
#     with level_2_2:
#         st.write('second column')
#         st.write('some content')
    
    
# app()          



