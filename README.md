Crypto Data Extractor

Descripción
Este proyecto es un programa en Python que permite extraer datos relacionados con criptomonedas de la API de CoinAPI. Proporciona métodos para obtener metadatos sobre intercambios de criptomonedas, así como datos históricos de precios de Bitcoin frente al dólar estadounidense. Además, incluye funcionalidades para realizar extracciones completas e incrementales de datos, guardando los resultados en archivos Parquet para su posterior análisis.

Funcionalidades
Extracción completa de datos: Obtención de metadatos sobre intercambios de criptomonedas y datos históricos de precios de Bitcoin.
Extracción incremental de datos: Actualización diaria de los datos históricos de precios de Bitcoin.
Conversión de datos a DataFrames de Pandas para su manipulación y análisis.
Guardado de datos en formato Parquet para un almacenamiento eficiente y comprimido.
Requisitos
Python 3.x
Paquetes requeridos: requests, pandas, pyarrow
Uso
Clona este repositorio o descarga el código fuente.
Instala los paquetes requeridos ejecutando pip install -r requirements.txt.
Configura la variable api_key con tu clave de API de CoinAPI.
Ejecuta python crypto_data_extractor.py para iniciar la extracción de datos.
Contribuciones
¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Haz tus cambios y confirma (git commit -am 'Agrega nueva característica').
Sube la rama (git push origin feature/nueva-caracteristica).
Abre un Pull Request.
