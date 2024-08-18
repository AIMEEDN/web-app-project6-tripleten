import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Aplicación web')

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", title= "Kilometraje")
    st.plotly_chart(fig,use_container_width=True)

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price", title= "Kilometraje Vs Precio")
    st.plotly_chart(fig, use_container_width=True)
