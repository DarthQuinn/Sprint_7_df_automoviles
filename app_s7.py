
import pandas as pd
import streamlit as st
import plotly.express as px

#cargar datos / Load data
df_car = pd.read_csv('vehicles_us.csv') 

df_car = df_car.dropna(subset=['price', 'odometer']) # Si no hay valores en 'price' y 'odometer' no nos sirven para el analisis

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # clic en el botón
         # escribir un mensaje
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
     fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    