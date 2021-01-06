import streamlit as st
from Scripts.streamlit_graph import graph_generator
from Scripts.streamlit_covid import show_map
import pandas as pd
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def load_data(Path):
    return pd.read_csv(Path)

if __name__ == "__main__":

    seccion = st.sidebar.selectbox(
        "Sección:",
        ('Introducción','Graph', 'COVID')
    )

    if seccion == 'Introducción':
        introduccion_ = read_markdown_file('README.md')
        st.markdown(introduccion_, unsafe_allow_html=True)

    elif seccion == 'Graph':
        graph_markdown = read_markdown_file('Sections/graphviz.md')
        st.markdown(graph_markdown, unsafe_allow_html=True)
        graph_generator()

        expander = st.beta_expander('Tarea')
        graph_homework= read_markdown_file('Homeworks/GraphvizHomework.md',)
        expander.write(graph_homework)
        
    elif seccion == 'COVID':
        graph_markdown = read_markdown_file('Sections/EDA_covid.md')
        st.markdown(graph_markdown, unsafe_allow_html=True)   

        Datos_confirmados =  pd.read_csv('Datasets/JohnsHopkins/Custom/Confirmados_Acumulado.csv')
        posicion = pd.read_csv('Datasets/JohnsHopkins/Custom/Posicion_pais.csv', index_col = 'Country/Region')

        show_map(Datos_confirmados, posicion,"confirmado")

        expander = st.beta_expander('Tarea')
        covid_homework= read_markdown_file('Homeworks/EDAHomework.md',)
        expander.write(covid_homework)