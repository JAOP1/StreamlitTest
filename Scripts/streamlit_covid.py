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
    raise NotImplementedError

