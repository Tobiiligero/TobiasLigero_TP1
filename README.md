Inicio del programa: Creamos un programa en Python que nos ayudará a obtener datos sobre criptomonedas de una fuente llamada CoinAPI. Queremos extraer estos datos para poder analizarlos más tarde.

Conexión con CoinAPI: Utilizamos una biblioteca llamada requests para comunicarnos con CoinAPI a través de internet. Esto nos permite pedirles los datos que necesitamos.

Obtención de datos: Hacemos una solicitud a CoinAPI para obtener los datos que queremos. Podemos pedirles datos sobre los intercambios de criptomonedas y también datos históricos de precios de Bitcoin.

Procesamiento de datos: Una vez que obtenemos los datos de CoinAPI, los convertimos en un formato que Python pueda entender fácilmente. Esto nos facilita trabajar con los datos y hacer cosas como análisis o visualizaciones más tarde.

Guardado de datos: Después de procesar los datos, los guardamos en nuestro propio sistema de archivos en nuestro computador. Los guardamos en un formato especial llamado Parquet, que es eficiente para trabajar con grandes cantidades de datos.

Extracción completa: Realizamos una primera extracción de datos donde obtenemos todos los datos disponibles sobre los intercambios de criptomonedas y los precios históricos de Bitcoin. Esto nos da una visión general de los datos.

Extracción incremental: Luego, realizamos extracciones diarias para obtener los datos actualizados más recientes. Esto nos permite mantener nuestros datos al día sin tener que volver a obtener todos los datos cada vez.

Finalización del programa: Una vez que hemos terminado de obtener y procesar los datos, el programa imprime un mensaje indicando que hemos terminado.

En resumen, nuestro programa se encarga de obtener datos sobre criptomonedas de CoinAPI, procesarlos y guardarlos en nuestro computador para su uso futuro. Hacemos una extracción inicial para obtener todos los datos disponibles y luego realizamos extracciones diarias para mantenerlos actualizados.


Estas bibliotecas son comúnmente utilizadas en proyectos de análisis de datos en Python y son muy útiles para este tipo de tareas.

requests: Se utiliza para hacer solicitudes HTTP a la API de CoinAPI y obtener los datos necesarios.

pandas: Utilizada para manipular los datos en forma de DataFrames, lo que facilita su análisis y procesamiento.

pyarrow.parquet: Esta biblioteca proporciona funciones para trabajar con archivos Parquet, permitiendo guardar los datos en este formato eficiente y comprimido.

datetime: Importada para trabajar con fechas y tiempos, especialmente para realizar operaciones como obtener la fecha de ayer para la extracción incremental de datos.

api_key: Esta es la clave de API proporcionada por CoinAPI que se utiliza para autenticar las solicitudes a su servicio.

base_url: Es la URL base de la API de CoinAPI a la que se enviarán las solicitudes para obtener datos.

data_directory: Es el directorio donde se guardarán los archivos de datos. Por defecto, se establece como crypto_data_lake, pero puedes cambiarlo según tus preferencias.

Estas son las variables principales que se utilizan en el programa para configurar la conexión con la API, definir la ubicación de los archivos de datos y mantener la seguridad al utilizar la clave de API.
