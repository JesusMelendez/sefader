import streamlit as st
# from tools.indicadores import df_complete


#page
st.set_page_config(layout="wide",page_icon=f'🌽')
logo = './src/img/sefader_logo.png'
# cimmyt = './src/img/cimmyt_new.png'
cl,cl1,cl3,cl4 = st.columns(4)
cl.image(logo)
cimmyt_logo = "./src/img/cimmyt.png"
cl4.image(cimmyt_logo)



st.markdown(
    """
¡Hola y bienvenido a nuestro sistema de monitoreo de datos! 🎉 

Este sistema es gracias a la colaboración de la Secretaría de Fomento Agroalimentario y Desarrollo Rural (SEFADER) y el Centro Internacional de Mejoramiento del Maíz y el Trigo (CIMMYT). Esta diseñado para ofrecerte una herramienta poderosa y efectiva.
Aquí, podrás explorar y analizar los datos de los programas de **Abasto seguro de maíz y Autosuficiencia alimentaria**.

¿Qué encontrarás en tu panel?
1. Cobertura 🌍

Descubre las regiones y temporalidades en donde estos programas tienen presencia. Esta sección te permitirá identificar áreas clave y tendencias a lo largo del tiempo.

2. Seguimiento 📆

Accede a información valiosa sobre el número de visitas a productores, los temas abordados en talleres de capacitación. También podrás revisar los paquetes tecnológicos implementados, que ayudan a maximizar las estrategias de los programas implementados por la SEFADER.

3. Impacto ✅

Aquí medimos los costos, ingresos y la utilidad generada. Esta sección es esencial para evaluar el rendimiento generado.

4. Calidad de datos 🔍

Para nuestros usuarios más expertos, esta sección es crucial. Podrás detectar anomalías en los datos o identificar casos atípicos que podrían influir en los indicadores. 

Estamos aquí para apoyarte en cada paso del camino. Si tienes preguntas o necesitas ayuda, no dudes en contactarnos al correo j.melendez@cgiar.org

¡Explora cada rincón de nuestro sistema y aprovecha al máximo esta herramienta diseñada especialmente para ti! ¡Disfruta tu experiencia! 😊
        
        """)


st.balloons()


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