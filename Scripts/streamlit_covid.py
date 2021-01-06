import streamlit as st
import pandas as pd 
import pydeck as pdk
import numpy as np 

month_days = {'Enero':31,
              'Febrero':28,'Marzo':31, 
              'Abril':30, 'Mayo':31,
              'Junio':30,'Julio':30,
              'Agosto':31,'Septiembre':30,
              'Octubre':31,'Noviembre':30,'Diciembre':30}

month_to_num = {key: i+1 for i,key in enumerate(month_days)}
num_to_month = {(i+1): key for i,key in enumerate(month_days)}

def show_map(df_,coords,str_):

    left_col , right_col = st.beta_columns(2)

    with left_col:
        start_, end_ = st.select_slider(
            'Meses de estudio:',
            options=list(month_days.keys()),
            value= ('Enero','Diciembre')
        )

    with right_col:

        population= st.number_input(
            "Población:",
            min_value=2,
            max_value=400000,
            step=1
        )

    st.write('Casos en los meses: '+start_ + ' a ' + end_ + ' con al menos ' + str(population) + ' casos confirmados')

    month_ = month_to_num[start_] - 1

    if month_ < 1:
        start_string = '1/1/20'
    else:
        start_string = '%d/%d/20' % (month_, month_days[ num_to_month[month_]])
    
    end_string = '%d/%d/20' % (month_to_num[end_], month_days[end_])


    casos_confirmados = df_.loc[:, ['Country/Region', end_string]]
    casos_confirmados[end_string] -= df_[start_string]

    casos_confirmados = casos_confirmados[ casos_confirmados[end_string] >= population]
    coord_datos = coords.loc[casos_confirmados['Country/Region']]

    nuevo_ = coord_datos.reset_index()
    nuevo_ =  nuevo_.drop(columns=['Country/Region'])
    print(nuevo_.head(10))
    st.pydeck_chart(
        pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state = pdk.ViewState(
                latitude = 19.4978,
                longitude=-99.1269,
                zoom=4,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'ScatterplotLayer',
                    data= nuevo_,
                    get_position='[lon,lat]',
                    get_fill_color='[200,30,0,160]',
                    get_radius= 150000,
                ),
            ]
        )
    )