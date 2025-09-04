# Proyecto Sprint 7 - Herramientas de desarrollo de software

## **Exploración de Ventas de Vehículos**

Esta aplicación web fue desarrollada en **Python** utilizando librerías como: **Streamlit**, **Pandas** y **Plotly.** El objetivo es analizar y visualizar un conjunto de datos de vehículos listados para la venta en EE. UU.

El dataset utilizado tiene como nombre: "**vehicles_us.csv"** y contiene información sobre vehículos listados para la venta en EE. UU. Incluye las siguientes columnas:

* Año del modelo
* Precio
* Tipo de combustible
* Condición
* Transmisión
* Odómetro
* Tipo de vehículo

La aplicación permite explorar las características principales de los autos disponibles y descubrir patrones relacionados con su precio, condición, transmisión, combustible, año de modelo, entre otros.

## Funcionalidades principales

- 📊 **Vista previa del dataset**: muestra una tabla exploratoria con registros aleatorios de los vehículos.
- 💰 **Promedio de precios por año del modelo**: gráfico interactivo con filtros de rangos de años.
- 🚘 **Cantidad de autos listados por categorías**: visualización de autos por condición, tipo de combustible y transmisión.
- 💵 **Distribución de precios por categorías**: histogramas interactivos de precios según combustible, transmisión y condición.
- 🚙 **Distribución general**: histogramas del precio y lectura del odómetro, con estadísticas descriptivas.
- 📚 **Relación entre precio y otras variables**: gráficos de dispersión (scatter plots) entre el precio y categorías como condición, transmisión, tipo de vehículo, odómetro o año del modelo.

## ¿Cómo utilizar el proyecto?

1. Clona el repositorio en tu computadora local:

```bash
git clone <url-del-repositorio>
```

2. Instala las librerías necesarias:

```bash
pip install -r requirements.txt
```

    3. Ejecuta la aplicación desde la terminal con streamlit:

```bash
streamlit run app.py
```

    4. También puedes acceder a tráves del servicio web en render con el siguiente vínculo:
