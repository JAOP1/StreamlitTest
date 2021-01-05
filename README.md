# Introducción a Streamlit
Antes de comenzar es necesario instalar:
* streamlit==0.69.0 (esta versión en específico para utilizar pydeck)
* graphviz
* pydeck
 
Los siguientes dos apartados son para mostrar el uso de la librería de Graphviz para
mostrar grafos y por otro lado, hacer visualización del estado actual de los casos
relacionados con *COVID-19*.

Aprenderás paso a paso como fue desarrollado este proyecto, sin embargo, te invitamos a revisar la documentación que se encuentra en [streamlit](https://docs.streamlit.io/en/stable/api.html).

En caso de que tengas interés en revisar casos de aplicación, puedes revisar un proyecto que tiene el código disponible en [github](https://github.com/streamlit/demo-self-driving) para detección de objectos.
 
 
 
La estructura del proyecto es:
```
🗀 StreamlitProject
│   main.py
└─── 🗀 Sections
│   │   graphviz.md
│   │   introduction.md
│  
└─── 🗀 Homeworks
│   │   GraphvizHomework.md  
│
└─── 🗀 Scripts
│   │   streamlit_graph.py
│   │   streamlit_covid.py
└─── 🗀 Datasets
│   │  🗀 JohnsHopkins
```
 
Después de haber instalado todo lo mencionado, para ejecutar el proyecto es:
 
```
streamlit run main.py
```