
import pandas as pd
import streamlit as st
import plotly.express as px




st.title("Bienvenido a mi app con fondo personalizado")
st.write("¡El fondo ahora tiene un degradado azul oscuro!")



st.header('demostracion de los conociemientos acerca de uso de desarollo de sofware para realizar paginas web')
st.write('Esta paguna web solo muestra graficas sobre el conjunto de datos de automoviles')

#"""Agregar un titulo y un encabezado"""

st.header('Automobile Data Analysis') 
st.write('Los datos de los vehiculos aqui mostrados son obtenidos de la pagina web https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data?resource=download')
st.header('Segundo encabezado sobre los coches') 
st.subheader('Se muestran gracias combinando columnas del dataset, no hay una analisis riguroso al cual se quiera llegar o demostrar aqui')


#cargar datos / Load data

df_car = pd.read_csv('vehicles_us.csv') 

df_car = df_car.dropna(subset=['price', 'odometer']) # Si no hay valores en 'price' y 'odometer' no nos sirven para el analisis


#Boton para hacer un histograma

st.write('Construir un histograma para la columna odómetro:')
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # clic en el botón
         # escribir un mensaje
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
     fig = px.histogram(df_car, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

#Boton para una segunda grafica de barras:

df_colorcar = df_car.groupby('paint_color').size()

st.write('Construir un gráfico de barras para la columna color:')
bar_button = st.button('Construir gráfico de barras')

if bar_button:
     color_fig = px.bar(df_colorcar,
                    x=df_colorcar.index,
                    y=df_colorcar.values, 
                    labels={'x': 'Color', 'y': 'Count'}, 
                    title='Count of Cars by Color')
     color_fig.update_traces(marker_color="#471fb4") #color morado
     st.plotly_chart(color_fig, use_container_width=True)

#Crear una casilla de verificación

build_scatter = st.checkbox('Construir el histograma')

if build_scatter: # si la casilla de verificación está seleccionada
     st.write('Construir un histograma para la columna odómetro:')

     fig_scatter = px.scatter(df_car, x="odometer", y="price") # crear un gráfico de dispersión
     st.plotly_chart(fig_scatter, use_container_width=True)


color_scatter = st.checkbox('Construir gráfico de dispersión con el precio y los dias listados')

if color_scatter: # si la casilla de verificación está seleccionada
     days_scatter = px.scatter(df_car,
                        x="days_listed",
                        y="price",
                        labels={'days_listed': 'Days Listed', 'price': 'Price'},
                        title='Price vs Days Listed') 
     days_scatter.update_traces(marker_color="#ee1d1d") 
     st.plotly_chart(days_scatter, use_container_width=True)
