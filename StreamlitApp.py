#Librerias Importadas
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np 
import pandas as pd 
import re
import plotly.express as px
import streamlit as st 
import requests
import plotly.graph_objects as go
from PIL import Image

st.sidebar.header('Syafiq Web App')

#Menú de la Barra Lateral
with st.sidebar: 
    selected = option_menu(
        menu_title=None,
        options=['Editor','Programas Internacionales','Analísis'],
    )


#Primera Página
if selected == 'Editor':
    st.title(f'Sofía Almeraya Gaona')
    st.markdown('Matrícula: A01283713')
    st.markdown('Pagína Web diseñada para el proyecto del Tecnologico de Monterrey')

    
    image = Image.open(r'/Users/sofiaalmeraya/Desktop/ActM1/ProgramasInt/Sofi.jpg')
    st.image(image, width=400)


#Segunda Página
if selected == 'Programas Internacionales':
    st.title(f'Programas Internacionales Proyecto')

    st.write('El departamento de Programas Internacionales del Tecnologíco de Monterrey tiene diferentes programas para la internacionalización de los estudiantes y durante este proyecto se trabajo con la base de datos para mostrar los siguientes highlights, estadisticas y visualización de resultados')

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')

    st.subheader('Tendencias de Internacionalización')

    # Row A
    col1, col2, col3 = st.columns(3)
    col1.metric("Estudiantes", "26,466")
    col2.metric("Paises", "56")
    col3.metric("Universidades", "774")

    st.markdown(' ')
    st.markdown(' ')

    #Titúlo Gráfico Campus
    st.subheader('Ubicación de Campus')


    #Gráfica Campus/país
    Grafcampus = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/ProgramasInt/PIdf_3.csv')
    repo_url = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json' 
    #Archivo GeoJSON
    mx_regions_geo = requests.get(repo_url).json()

    fig = px.choropleth(data_frame=Grafcampus, 
                        geojson=mx_regions_geo, 
                        locations=Grafcampus['Campus'], # nombre de la columna del Dataframe
                        featureidkey='properties.name',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                        color='Número de Estudiantes', #El color depende de las cantidades
                        color_continuous_scale="Brwnyl"
                        #scope="north america"
                   )

    fig.update_geos(showcountries=True, showcoastlines=True, showland=False, fitbounds="locations")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)



    #Titúlo Gráfico Nivel
    st.subheader('Nivel de Estudios de los Estudiantes')

    #Gráfica Nivel
    df2 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/ProgramasInt/PIdf_6.csv')
    fig2 = px.bar(df2, x='Nivel', y='Número de Estudiantes',
            hover_data=['Nivel','Número de Estudiantes'], color='Número de Estudiantes',
            color_continuous_scale="Brwnyl",
            labels={'Nivel de Estudios':'Cantidad de Estudiantes'}, height=400)

    fig2.update_layout(yaxis_type="log")
    st.plotly_chart(fig2, use_container_width=True)



    #Titúlo Gráfico Tipo
    st.subheader('Tipo de Programas')
    
    #Gráfica Tipo
    df3 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/ProgramasInt/PIdf_5.csv')
    fig3 = px.bar(df3, x="Número de Estudiantes", y="Tipo", orientation='h')

    fig3.update_layout(xaxis_type="log")
    fig3.update_traces(marker_color='moccasin')
    st.plotly_chart(fig3, use_container_width=True)



    #Titúlo Gráfico Campus
    st.subheader('Campus de donde se Internacionalizan los Estudiantes')

    #Gráfica Campus
    df6 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/ProgramasInt/PIdf_9.csv')

    fig6 = px.scatter(df6, x="Campus", y="Número de Estudiantes",
	         size="Número de Estudiantes", color="Campus",
             hover_name="Campus", log_y=True, size_max=60)


    fig6.update_traces(marker_color='moccasin')
    st.plotly_chart(fig6, use_container_width=True)

#Tercera Página
if selected == 'Analísis':
    st.title(f'Estadísticas Internacionales')

    
    #Titúlo Gráfico Escuela
    st.subheader('Escuelas que más internacionalizan estudiantes')

    #Gráfica Escuela
    df4 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/ProgramasInt/PIdf_7.csv')
    fig4 = px.pie(df4, values='Número de Estudiantes', names='Escuela', color_discrete_sequence=px.colors.sequential.Brwnyl)
    fig4.update_traces(textinfo='percent+label')
    st.plotly_chart(fig4, use_container_width=True)


    #Titúlo Gráfico Pais
    st.subheader('Paises que forman parte de los programas')

    #Gráfica Pais
    df5 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/ProgramasInt/PIdf_4.csv')
    repo_url = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json' 
    #Archivo GeoJSON
    regions_geo = requests.get(repo_url).json()

    #st.sidebar.subheader('Mapa Parametros')
    #plot_data = st.sidebar.multiselect('Select data', df5['Pais'])

    fig5 = px.choropleth(data_frame=df5, 
                    geojson=regions_geo, 
                    locations=df5['Pais'], # nombre de la columna del Dataframe
                    featureidkey='properties.name',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='Número de Estudiantes', #El color depende de las cantidades
                    color_continuous_scale="Brwnyl",
                    #scope="north america"
                   )

    fig5.update_geos(showcountries=True, showcoastlines=True, showland=False, fitbounds="locations")
    fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig5, use_container_width=True)

    



    #Titúlo Gráfico Comparacion
    st.subheader('Estudiantes Asignados con su Primera Oportunidad')


    #Gráfica Comparacion
    df7 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/ProgramasInt/PIdf_12.csv')
    fig7 = px.pie(df7, values='Cantidad',names='Comparacion',color_discrete_sequence=px.colors.sequential.Brwnyl)
    fig7.update_traces(textinfo='percent+label')
    st.plotly_chart(fig7, use_container_width=True)



    #Titúlo Gráfico INT o SA
    st.subheader('Intercambio Tradicional ó Study Abroad')


    #Gráfica INT o SA
    df8 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/ProgramasInt/PIdf_10.csv')
    fig8 = px.bar(df8, x='Tipo', y='Número de Estudiantes',
             hover_data=['Tipo','Número de Estudiantes'], color='Número de Estudiantes',
             color_continuous_scale="Brwnyl",
             labels={'Nivel de Estudios':'Cantidad de Estudiantes'}, height=400)
             
    st.plotly_chart(fig8, use_container_width=True)
