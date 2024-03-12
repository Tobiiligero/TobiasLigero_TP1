{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0ee86fce-5988-46e3-99d7-8a2fcc9118e9",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Iniciando extracción completa de datos de criptomonedas...\n",
      "Datos guardados correctamente como archivo Parquet en crypto_data_lake\\crypto_metadata\\crypto_metadata.parquet.\n",
      "Datos guardados correctamente como archivo Parquet en crypto_data_lake\\crypto_historical_data\\crypto_historical_data.parquet.\n",
      "Extracción completa de datos finalizada.\n",
      "Iniciando extracción incremental de datos de criptomonedas...\n",
      "Error al obtener datos del endpoint /ohlcv/BITSTAMP_SPOT_BTC_USD/history?time_start=2024-03-10T00:00:00\n",
      "No se encontraron nuevos datos para extraer.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import requests\n",
    "import pandas as pd\n",
    "import pyarrow.parquet as pq\n",
    "from datetime import datetime, timedelta\n",
    "\n",
    "class CryptoDataExtractor:\n",
    "    def __init__(self, api_key):\n",
    "        self.base_url = 'https://rest.coinapi.io/v1'\n",
    "        self.api_key = api_key\n",
    "        self.data_directory = 'crypto_data_lake'\n",
    "\n",
    "    def fetch_data_from_api(self, endpoint):\n",
    "        url = self.base_url + endpoint\n",
    "        headers = {'X-CoinAPI-Key': self.api_key}\n",
    "        response = requests.get(url, headers=headers)\n",
    "        if response.status_code == 200:\n",
    "            data = response.json()\n",
    "            return data\n",
    "        else:\n",
    "            print(f\"Error al obtener datos del endpoint {endpoint}\")\n",
    "            return None\n",
    "\n",
    "    def convert_to_dataframe(self, data):\n",
    "        if data:\n",
    "            df = pd.DataFrame(data)\n",
    "            return df\n",
    "        else:\n",
    "            return None\n",
    "\n",
    "    def save_to_parquet(self, df, directory, filename):\n",
    "        if not os.path.exists(directory):\n",
    "            os.makedirs(directory)\n",
    "        file_path = os.path.join(directory, filename)\n",
    "        if df is not None:\n",
    "            df.to_parquet(file_path, engine='pyarrow')\n",
    "            print(f\"Datos guardados correctamente como archivo Parquet en {file_path}.\")\n",
    "        else:\n",
    "            print(\"No hay datos para guardar.\")\n",
    "\n",
    "    def extract_full_data(self):\n",
    "        print(\"Iniciando extracción completa de datos de criptomonedas...\")\n",
    "        metadata = self.fetch_data_from_api('/exchanges')\n",
    "        metadata_df = self.convert_to_dataframe(metadata)\n",
    "        self.save_to_parquet(metadata_df, os.path.join(self.data_directory, 'crypto_metadata'), 'crypto_metadata.parquet')\n",
    "\n",
    "        historical_data = self.fetch_data_from_api('/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1DAY')\n",
    "        historical_df = self.convert_to_dataframe(historical_data)\n",
    "        self.save_to_parquet(historical_df, os.path.join(self.data_directory, 'crypto_historical_data'), 'crypto_historical_data.parquet')\n",
    "        print(\"Extracción completa de datos finalizada.\")\n",
    "\n",
    "    def extract_incremental_data(self):\n",
    "        print(\"Iniciando extracción incremental de datos de criptomonedas...\")\n",
    "        # Supongamos que la API proporciona datos diarios actualizados una vez al día\n",
    "        yesterday_date = datetime.now() - timedelta(days=1)\n",
    "        formatted_date = yesterday_date.strftime('%Y-%m-%d')\n",
    "        updated_data = self.fetch_data_from_api(f'/ohlcv/BITSTAMP_SPOT_BTC_USD/history?time_start={formatted_date}T00:00:00')\n",
    "        updated_df = self.convert_to_dataframe(updated_data)\n",
    "        if updated_df is not None and not updated_df.empty:  # Verifica si hay datos y si no está vacío\n",
    "            self.save_to_parquet(updated_df, os.path.join(self.data_directory, 'crypto_daily_data', formatted_date), 'crypto_daily_data.parquet')\n",
    "            print(\"Extracción incremental de datos finalizada.\")\n",
    "        else:\n",
    "            print(\"No se encontraron nuevos datos para extraer.\")\n",
    "\n",
    "def main():\n",
    "    api_key = '4ADF70B7-F58E-4089-AE0D-958AE7D10440'\n",
    "    extractor = CryptoDataExtractor(api_key)\n",
    "    extractor.extract_full_data()  # Extracción completa\n",
    "    extractor.extract_incremental_data()  # Extracción incremental\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
