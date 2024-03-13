from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Especifica la ruta del archivo Parquet
    ruta_archivo_parquet = "C:/Users/Tobi/Desktop/DataIngVid/Tablas/Proyecto/crypto_data_lake/crypto_metadata/crypto_metadata.parquet"

    # Lee el archivo Parquet
    datos = pd.read_parquet(ruta_archivo_parquet)

    # Convertir los datos a HTML
    tabla_html = datos.to_html()

    return render_template('index.html', tabla_html=tabla_html)

if __name__ == '__main__':
    app.run(debug=True)
