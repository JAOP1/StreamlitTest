# Análisis exploratorio de datos
En este apartado vamos a trabajar con los datos proporcionados por la universidad
de John Hopkins. Los puedes encontrar en el sitio de [kaggle](https://www.kaggle.com/antgoldbloom/covid19-data-from-john-hopkins-university).
 
Los datos se encuentran dividido en *RAW* y *CONVENIENT*.
* Los atributos que tienen es Country/Region, 1/22/20, ..., 12/30/20. Es decir, cada columna representa el número de casos confirmados o muertes por cada país.
 
Es importante notar que los datos que tienen *RAW* son aquellos datos donde tienen la suma acumulada hasta ese día, mientras que en *CONVENIENTE* te muestran los casos registrados en ese día, además, tenemos un archivo con el nombre *CONVENIENT_global_metada.csv*, este archivo tiene toda la información sobre la latitud y longitud.
 
En este ejercicio, hemos realizado el preprocesamiento y se encuentra en 🗀 Datasets/JohnHopkins/custom/
