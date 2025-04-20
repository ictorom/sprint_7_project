import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Encabezado
st.header('Visualización interactiva de datos de vehículos')

# Casilla para histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma del odómetro de los vehículos en venta')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Casilla para gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión precio vs odómetro'):
    st.write('Relación entre precio y odómetro')
    fig = px.scatter(car_data, x='odometer', y='price', color='condition')
    st.plotly_chart(fig, use_container_width=True)
