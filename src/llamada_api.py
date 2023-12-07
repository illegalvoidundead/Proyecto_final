# Defino la URL base y los encabezados de la petición
base_url = 'https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{}/fechafin/{}/todasestaciones'
headers = {
    'accept': 'application/json',
    'api_key': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkYWxlZG9ndUBnbWFpbC5jb20iLCJqdGkiOiJkZGUwNTdiOC0zNzFhLTRkZDktYjUxOC1kNTVmM2RjZjkwYTYiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwMTE4MTI5NCwidXNlcklkIjoiZGRlMDU3YjgtMzcxYS00ZGQ5LWI1MTgtZDU1ZjNkY2Y5MGE2Iiwicm9sZSI6IiJ9.QJn-MC0QM108vEdzEx13iYWTp4CxReytcOiED8R0q10'
}

# Defino las fechas de inicio y fin en fecha de Python
start_date = datetime(1973, 1, 1)
end_date = datetime(2023, 1, 1)

# Inicializo una lista para almacenar los datos
data = []

while start_date < end_date:
    # Calculo la fecha agregando un período de 31 días a la fecha inicial
    request_end_date = start_date + timedelta(days=31)

    # Me aseguro de que "request_end_date" no exceda "end_date"
    if request_end_date > end_date:
        request_end_date = end_date

    # Formateo las fechas como strings en el formato requerido por la API
    start_date_str = start_date.strftime('%Y-%m-%dT%H:%M:%SUTC')
    end_date_str = request_end_date.strftime('%Y-%m-%dT%H:%M:%SUTC')

    # Construyo la URL de la solicitud
    url = base_url.format(start_date_str, end_date_str)

    try:
        # Petición GET a la API
        response = requests.get(url, headers=headers)

        # Compruebo si la petición fue exitosa
        if response.status_code == 200:
            # La API devuelve una URL en la respuesta que debes seguir para obtener los datos
            data_url = response.json()['datos']

            # Hago una segunda petición GET a la URL de los datos
            data_response = requests.get(data_url)

            # Compruebo si la segunda petición fue exitosa
            if data_response.status_code == 200:
                # Añado los datos a la lista
                data.extend(data_response.json())
            else:
                print(f'Error when accessing data URL: {data_response.status_code}')
        else:
            print(f'Error: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Exception when making GET request: {e}')

    # Incremento la fecha de inicio para la próxima iteración
    start_date = request_end_date

    # Introduzco una pausa de 1 segundo entre cada solicitud para evitar el error 429
    time.sleep(5)
