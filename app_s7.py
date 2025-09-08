
import pandas as pd
import streamlit as st
import plotly.express as px



st.header(f'<span clas="big-font">Automobile Data Analysis </span>') 

st.markdown(""" <style>
          .big-font {font-size:50px !important;
          }
          <style>
          """, unsafe_allow_html=True) # definir una clase CSS


st.markdown('<h2> Segundo encabezado sobre los coches </h2>', unsafe_allow_html=True) # encabezado con HTML


#cargar datos / Load data

df_car = pd.read_csv('vehicles_us.csv') 

df_car = df_car.dropna(subset=['price', 'odometer']) # Si no hay valores en 'price' y 'odometer' no nos sirven para el analisis

"""
Boton para hacer un histograma
"""

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # clic en el botón
         # escribir un mensaje
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
     fig = px.histogram(df_car, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

"""
Crear una casilla de verificación
"""

build_histogram = st.checkbox('Construir el histograma')

if build_histogram: # si la casilla de verificación está seleccionada
     st.write('Construir un histograma para la columna odómetro:')

     fig_1 = px.histogram(df_car, x="odometer") # crear un histograma
     st.plotly_chart(fig_1, use_container_width=True)
     fig_scatter = px.scatter(df_car, x="odometer", y="price") # crear un gráfico de dispersión
     fig_scatter.show() 
