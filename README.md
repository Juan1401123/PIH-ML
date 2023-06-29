# PIH-ML-Proyecto de Machine Learning Recomendación por Similitud y APPI de Consulta de Películas 
El objetivo de este proyecto es brindar acceso a una amplia base de datos de películas y sus calificaciones, permitiendo su filtrado a través de varias funciones mediante una API. Además, se implementará un sistema de recomendación basado en la similitud de películas, utilizando la mencionada base de datos.

El objetivo de este proyecto es brindar acceso a una amplia base de datos de películas y sus calificaciones, permitiendo su filtrado a través de varias funciones mediante una API. Además, se implementará un sistema de recomendación basado en la similitud de películas, utilizando la mencionada base de datos.

Este repositorio está preparado para su despliegue mediante Render.

El proceso de desarrollo del proyecto consta de las siguientes etapas:
1.ETL (Extract, Transform, Load): Se realizó un proceso de extracción, transformación y carga de los datos para que puedan ser consumidos por la API. Dado que algunas partes de los datos se encontraban en formatos complicados de acceder, se llevó a cabo esta etapa para facilitar su utilización.
2.EDA (Exploratory Data Analysis): Se llevó a cabo un análisis exploratorio de los datos para implementar el desarrollo del modelo de similitud. Esta etapa permitió comprender la estructura y características de los datos, así como identificar patrones relevantes para el sistema de recomendación.
3.Se utilizó FASTAPI y Render para el despliegue de la API. FASTAPI es un marco de desarrollo web rápido para Python, y Render es una plataforma que facilita el despliegue de aplicaciones y servicios en la nube.
4.Se desarrollaron seis funciones de consulta para el consumo de los datos. Cinco de estas funciones se enfocaron en la consulta y filtrado de la información de las películas, mientras que la última función se encargó de la consulta del modelo de similitud.
En resumen, el objetivo principal de este proyecto es proporcionar acceso a una base de datos de películas y calificaciones, permitiendo filtrar la información mediante varias funciones en una API. Además, se implementa un sistema de recomendación basado en la similitud de películas. El proceso de desarrollo involucra un ETL para facilitar el acceso a los datos, un análisis exploratorio de los mismos, el uso de FASTAPI y Render para el despliegue, y la creación de varias funciones de consulta.
