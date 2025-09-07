
import pandas as pd
import streamlit as st
import plotly.express as px

#cargar datos / Load data
df_car = pd.read_csv('vehicles_us.csv') 

df_car = df_car.dropna(subset=['price', 'odometer']) # eliminar filas con valores nulos en las columnas 'price' y 'odometer'