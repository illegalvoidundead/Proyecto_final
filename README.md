# Proyecto final

![girl_testing_weather_md_clr](https://github.com/illegalvoidundead/Proyecto_final/assets/143459249/31ca36bd-3d66-4115-a53b-e9b5bdcbcb65)

## Descripción
Este proyecto tiene como objetivo analizar la evolución de las temperaturas y precipitaciones en diferentes regiones de España utilizando datos proporcionados por AEMET (Agencia Estatal de Meteorología), así como el uso de recursos hídrigcos destinado a la agricultura. 

Mediante Python y utilizando la API de AEMET y su librería cliente, he obtenido datos climáticos de estaciones específicas y realizado un análisis exploratorio para entender mejor las tendencias a lo largo del tiempo.

![tongueleft](https://github.com/illegalvoidundead/Proyecto_final/assets/143459249/6a7614f7-fdf5-4f07-a19c-dec384c11a55)

<details>
<summary>Función para obtener datos climatológicos a través de la librería cliente de la AEMET</summary>

[![Captura de pantalla 2023-12-07 a las 17 05 10](https://github.com/illegalvoidundead/Proyecto_final/assets/143459249/35d282c2-78db-41d2-91bb-cfbbd8b391ca)](https://github.com/illegalvoidundead/Proyecto_final/blob/main/code/python-aemet.ipynb)


</details>

He utilizado la librería Pandas para realizar la limpieza y el procesamiento de los datos, eliminando caracteres no deseados, seleccionando columnas de interés, creando DataFrames con diferentes registros, formateando fechas, convirtiendo valores y eliminando los valores NaN, procurando siempre mantener la integridad de los datos.

Los resultados procesados han sido guardados en archivos CSV para un análisis y visualización posterior.

## Resultados

Análisis exploratorio de datos climáticos.

Visualizaciones: gráficos de la evolución de temperaturas y precipitaciones en las ciudades seleccionadas.

<details>
<summary>Gráfico de temperaturas</summary>

![Captura de pantalla 2023-12-07 a las 16 53 17](https://github.com/illegalvoidundead/Proyecto_final/assets/143459249/012e689e-8478-4bbd-b7a5-693d6d085ecb)

</details>

## Esctructura de carpetas


* code: contiene hojas de jupyter notebook
* dashboard: contiene la visualización de Tableau
* datasets: contiene los archivos CSV generados 
* img: contiene las imagenes utilzadas tanto en la visualización como en el README
* src: contiene código fuente
* raíz:

  .gitignore: especifica que archivos y carpetas se ignorarán en git
  
  README.MD: markdown que contiene la descripción del repositorio


## Contribuciones y Mejoras Futuras
Posibilidad de ampliar el análisis a más ciudades o periodos temporales.
Mejoras en la visualización y presentación de resultados.

## Autor
David Ledo Guillén

![mon_chart](https://github.com/illegalvoidundead/Proyecto_final/assets/143459249/986f32bb-d9a9-4372-b3e0-9f3a9caab327)

