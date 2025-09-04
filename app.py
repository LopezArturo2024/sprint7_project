import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# Leer los datos del archivo CSV
# -----------------------------------------------
car_data = pd.read_csv('vehicles_us.csv')


# Título de la aplicación
# -----------------------------------------------
st.title("🚘  Exploración de ventas de vehículos")
st.write("¡Bienvenido!")
st.write(""" Esta esta app te permitirá conocer a profundidad los diferentes vehículos listados para la venta. 
        A través de diferentes visualizaciones podrás encontrar e identifcar patrones de precio según las diferentes 
        categorías registradas.""")


# 1. Tabla exploratoria de los datos
# -----------------------------------------------
st.subheader("📊 Vista previa del dataset")
st.write("""Primero conozcamos un poco nuestros datos""")
st.dataframe(car_data.sample(10))


# 2. Gráfico de barras del promedio de precios por año modelo del vehículo
# -----------------------------------------------
st.subheader("💰 Promedio de precios de los vehículos listados")
st.write("De esta forma podemos revisar por años el costo promedio de los vehículos listados")

df_avg_precios = car_data.groupby('model_year')['price'].mean(
).reset_index().sort_values(by='price', ascending=False)

filtro = st.selectbox("Selecciona un rango de años:",
                      ("Todos", "2000 - 2010", "> 2010",
                       "1990 - 2000", "1980 - 1990", "< 1980")
                      )

if filtro == "2000 - 2010":
    df_filtrado = df_avg_precios.query(
        "model_year > 2000 and model_year <= 2010")
elif filtro == "> 2010":
    df_filtrado = df_avg_precios.query("model_year > 2010")
elif filtro == "1990 - 2000":
    df_filtrado = df_avg_precios.query(
        "model_year > 1990 and model_year <= 2000")
elif filtro == "1980 - 1990":
    df_filtrado = df_avg_precios.query(
        "model_year > 1980 and model_year <= 1990")
elif filtro == "< 1980":
    df_filtrado = df_avg_precios.query("model_year <= 1980")
else:
    df_filtrado = df_avg_precios.copy()

fig = go.Figure(data=[go.Bar(
    x=df_filtrado["model_year"], y=df_filtrado["price"],
    text=df_filtrado["price"].round(2)
)])

fig.update_layout(title_text=f"Precio promedio de los vehículos por año del modelo ({filtro})",
                  xaxis_title="Modelo del auto (Años)",
                  yaxis_title="Precio promedio (USD)",
                  uniformtext_minsize=6)

fig.update_traces(
    textposition="outside",
    textfont=dict(
        size=10,
        family="Arial Black"
    )
)
st.plotly_chart(fig, use_container_width=True)


# 3. Cantidad de autos listados por categorías (fuel, transmission, condition)
# -----------------------------------------------
st.subheader("🚘 Cantidad de autos listados por categoría")
st.write("Podemos encontrar la cantidad de autos listados según su condición, el tipo de combustible y su transmisión")

fuel_checkbox = st.checkbox('Listado por tipo de combustible')
condition_checkbox = st.checkbox('Listado por condición del vehículo')
transmission_checkbox = st.checkbox('Listado por tipo de transmisión')

if condition_checkbox:
    condition_vehicles = car_data['condition'].value_counts().reset_index()

    fig = go.Figure(data=[go.Bar(
        x=condition_vehicles["condition"], y=condition_vehicles["count"],
        text=condition_vehicles["count"]
    )])

    fig.update_layout(title_text="Listado de vehículos por condición",
                      xaxis_title="Condición del vehículo",
                      yaxis_title="Cantidad de vehículos listados",
                      uniformtext_minsize=6)

    fig.update_traces(
        textposition="outside",
        textfont=dict(
            size=10,
            family="Arial Black"
        )
    )

    st.plotly_chart(fig, use_container_width=True)

if fuel_checkbox:
    fuel_vehicles = car_data['fuel'].value_counts().reset_index()

    fig = go.Figure(data=[go.Bar(
        x=fuel_vehicles["fuel"], y=fuel_vehicles["count"],
        text=fuel_vehicles["count"]
    )])

    fig.update_layout(title_text="Listado de vehículos por tipo de combustible",
                      xaxis_title="Tipo de combustible",
                      yaxis_title="Cantidad de vehículos listados",
                      uniformtext_minsize=6)

    fig.update_traces(
        textposition="outside",
        textfont=dict(
            size=10,
            family="Arial Black"
        )
    )

    st.plotly_chart(fig, use_container_width=True)

if transmission_checkbox:
    transmission_vehicles = car_data['transmission'].value_counts(
    ).reset_index()

    fig = go.Figure(data=[go.Bar(
        x=transmission_vehicles["transmission"], y=transmission_vehicles["count"],
        text=transmission_vehicles["count"]
    )])

    fig.update_layout(title_text="Listado de vehículos por tipo de transmisión",
                      xaxis_title="Tipo de transmisión",
                      yaxis_title="Cantidad de vehículos listados",
                      uniformtext_minsize=6)

    fig.update_traces(
        textposition="outside",
        textfont=dict(
            size=10,
            family="Arial Black"
        )
    )

    st.plotly_chart(fig, use_container_width=True)


# 4. Distribución de precios por categorías (fuel, transmission, condition) - Histogramas
# -----------------------------------------------

st.subheader("💵 Distribución de precios por categorías")

fuel_button = st.button('Crear histograma de precios por tipo de combustible')
condition_button = st.button(
    'Crear histograma de precios por condición del vehículo')
transmission_button = st.button(
    'Crear histograma de precios por tipo de transmisión')

if fuel_button:
    fuel_options = list(car_data['fuel'].unique())

    st.write(
        "Contruyendo la distribución de precios para cada tipo de combustible de los vehículos listados")
    fig = go.Figure()

    for option in fuel_options:
        filtered_data = car_data[car_data['fuel'] == option]
        fig.add_trace(go.Histogram(
            x=filtered_data['price'], nbinsx=50, name=option))

    fig.update_layout(barmode='overlay',
                      title_text="Distribución de precios por tipo de combustible",
                      xaxis_title="Precio (USD)",
                      yaxis_title="Frecuencia",
                      uniformtext_minsize=6,
                      xaxis=dict(range=[0, 80000]))

    fig.update_traces(opacity=0.4)

    st.plotly_chart(fig, use_container_width=True)

if transmission_button:
    transmission_options = list(car_data['transmission'].unique())
    st.write(
        "Contruyendo la distribución de precios para cada tipo de transmisión de los vehículos listados")

    fig = go.Figure()

    for option in transmission_options:
        filtered_data = car_data[car_data['transmission'] == option]
        fig.add_trace(go.Histogram(
            x=filtered_data['price'], nbinsx=50, name=option))

    fig.update_layout(barmode='overlay',
                      title_text="Distribución de precios por tipo de transmisión",
                      xaxis_title="Precio (USD)",
                      yaxis_title="Frecuencia",
                      uniformtext_minsize=6,
                      xaxis=dict(range=[0, 80000]))

    fig.update_traces(opacity=0.4)
    st.plotly_chart(fig, use_container_width=True)


if condition_button:
    condition_options = list(car_data['condition'].unique())
    st.write(
        "Contruyendo la distribución de precios por cada tipo de condición de los vehículos listados")
    fig = go.Figure()

    for option in condition_options:
        filtered_data = car_data[car_data['condition'] == option]
        fig.add_trace(go.Histogram(
            x=filtered_data['price'], nbinsx=50, name=option))

    fig.update_layout(barmode='overlay',
                      title_text="Distribución de precios por condición del vehículo",
                      xaxis_title="Precio (USD)",
                      yaxis_title="Frecuencia",
                      uniformtext_minsize=6,
                      xaxis=dict(range=[0, 80000]))

    fig.update_traces(opacity=0.4)
    st.plotly_chart(fig, use_container_width=True)


# 5. Distribución general de precios y odómetro - Histogramas
# -----------------------------------------------
st.subheader("🚙 Histograma general de precios y odómetro")
st.write("Veamos como se comporta la distribución general de precios y la lectura del odómetro de los vehículos listados")

price_button = st.button('Crear histograma de precios')
odometer_button = st.button('Crear histograma del odómetro')

if price_button:
    st.write(
        "Contruyendo la distribución de precios general de los vehículos listados")
    fig = go.Figure(data=[go.Histogram(x=car_data['price'], nbinsx=50)])

    fig.update_layout(title_text="Distribución de precios de los vehículos listados",
                      xaxis_title="Precio (USD)",
                      yaxis_title="Cantidad de vehículos",
                      uniformtext_minsize=6,
                      xaxis=dict(range=[0, 150000]))

    st.plotly_chart(fig, use_container_width=True)

    st.write("Estadísticas descriptivas de los precios de los vehículos listados")
    price_statistics = car_data['price'].describe().round(2).reset_index()
    price_statistics.columns = ['Medida', 'Valor']
    st.dataframe(price_statistics)

if odometer_button:
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'], nbinsx=50)])

    fig.update_layout(title_text="Distribución de lectura del odómetro de los vehículos listados",
                      xaxis_title="Odómetro (millas)",
                      yaxis_title="Cantidad de vehículos",
                      uniformtext_minsize=6)

    st.plotly_chart(fig, use_container_width=True)

    st.write(
        "Estadísticas descriptivas de la lectura del odómetro de los vehículos listados")
    odometer_statistics = car_data['odometer'].describe().round(
        2).reset_index()
    odometer_statistics.columns = ['Medida', 'Valor']
    st.dataframe(odometer_statistics)


# 6. Relación entre el precio y categorías del vehículo (Scatter plots)
# -----------------------------------------------
st.subheader("📚 Relación entre el precio y categorías del vehículo")

filtro = st.selectbox("Selecciona la categoría que quieres analizar:",
                      ("Condición del vehículo", "Tipo de Transmisión",
                       "Tipo de vehículo", "odómetro", "Año del modelo")
                      )

if filtro == "Condición del vehículo":
    st.write(
        "Contruyendo la dispersión de precios según la condición del vehículo")
    fig = go.Figure(
        data=[go.Scatter(x=car_data['condition'], y=car_data['price'], mode='markers')])

    fig.update_layout(title_text="Dispersión de precio por condición del vehículo",
                      xaxis_title="Condición del vehículo",
                      yaxis_title="Precio (USD)",
                      uniformtext_minsize=6)
    st.plotly_chart(fig, use_container_width=True)

elif filtro == "Tipo de Transmisión":
    st.write(
        "Contruyendo la dispersión de precios según el tipo de transmisión del vehículo")
    fig = go.Figure(data=[go.Scatter(
        x=car_data['transmission'], y=car_data['price'], mode='markers')])

    fig.update_layout(title_text="Dispersión de precio por transmisión del vehículo",
                      xaxis_title="Transmisión del vehículo",
                      yaxis_title="Precio (USD)",
                      uniformtext_minsize=6)
    st.plotly_chart(fig, use_container_width=True)

elif filtro == "Tipo de vehículo":
    st.write("Contruyendo la dispersión de precios según el tipo de vehículo")
    fig = go.Figure(data=[go.Scatter(x=car_data['type'],
                    y=car_data['price'], mode='markers')])

    fig.update_layout(title_text="Dispersión de precio por tipo de vehículo",
                      xaxis_title="Tipo de vehículo",
                      yaxis_title="Precio (USD)",
                      uniformtext_minsize=6)
    st.plotly_chart(fig, use_container_width=True)

elif filtro == "odómetro":
    st.write(
        "Contruyendo la dispersión de precios según la lectura del odómetro del vehículo")
    fig = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    fig.update_layout(title_text="Dispersión de precio por recorrido del vehículo",
                      xaxis_title="Lectura del odómetro (millas)",
                      yaxis_title="Precio (USD)",
                      uniformtext_minsize=6)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.write(
        "Contruyendo la dispersión de precios según el año del modelo")
    fig = go.Figure(data=[go.Scatter(
        x=car_data['model_year'], y=car_data['price'], mode='markers')])

    fig.update_layout(title_text="Dispersión de precio por año del vehículo",
                      xaxis_title="Año del modelo",
                      yaxis_title="Precio (USD)",
                      uniformtext_minsize=6)
    st.plotly_chart(fig, use_container_width=True)
