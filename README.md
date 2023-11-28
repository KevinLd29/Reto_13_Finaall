# Reto 13, el final de un gran curso.

Ya estamos en el último reto que nos queda de este curso, fue una gran travesía pero la verdad este curso superó mis espectativas, y si, esto ya es una despedida, si quiero seguir programando pero yaserá aprender por mi propia cuenta.
Para este reto solo voy a desarrollar los puntos 4 y 5 de el reto propuesto por el profe, ya que por lo visto, son códigos extensos, pero sin más palabreos, hora de comenzar.

# Punto 4
Diosmio, este JSON que dolor de cabeza JAJA, no pude solo pero les cuento en que consiste:

**Analizar el pronóstico del clima:**

```python
import json
from datetime import datetime

# JSON con pronóstico del clima
weatherJsonString = '''
... (import json
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)) ...
'''

# Convertir JSON a diccionario de Python
weatherData = json.loads(weatherJsonString)

# Campos a revisar para alertas
alertFields = ['alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento']

# Iterar sobre los días en el pronóstico
for day in range(8):
    # Iterar sobre los campos de alerta
    for alertField in alertFields:
        # Obtener el valor de alerta para el día actual y el campo actual
        alertValue = weatherData[alertField][str(day)]

        # Si hay una alerta, imprimir detalles
        if alertValue != '-':
            alertDate = datetime.utcfromtimestamp(weatherData['dt'][str(day)]).strftime('%Y-%m-%d %H:%M:%S')
            alertMessage = f"Alerta el {alertDate}: Tipo: {alertField}, Valor: {alertValue}"
            print(alertMessage)

````

Mirando otros repos, afortunadamente el JSON no queda como una linea de una longitud super larga ocupando casi todo el repo SHJAHSJA, pero para trabajarlo en el VSCODE fue un completo dolor de cabeza.
Esta fue la solución que le pude dar, no estoy muy familiarizado con los JSON, pero logro medio entender su funcionamiento y como tratarlos. Este código es bastante corto ¿no? (Sarcasmo), pero bueno, este programa analiza el pronóstico del clima en formato JSON para encontrar y mostrar alertas climáticas específicas para cada día. Una explicación podría ser:

- Se utiliza el módulo `json` para cargar el JSON del pronóstico del clima en una estructura de datos de Python.
- Se define una lista llamada `alertFields` que contiene los campos en los que se buscarán alertas.
- Se itera sobre cada día en el pronóstico y, para cada día, se revisan los campos de alerta definidos.
- Si se detecta una alerta (indicada por un valor diferente de '-' en el campo correspondiente), se imprime la fecha del día, el tipo de alerta y su valor asociado.


# Punto 5

En este putno es necesario tener ciertas bases en uso del JSON, cosa que antes del desarrollo de este reto, no tenía, no los donimo pero que fortuna que ya logro comprenderlos, bueno, entonces:

**Conectar a al menos 3 API's:**

```python
import requests

# Ejemplos de URL de API (sustituir con las URL reales de las API que desees consultar)
apiUrls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/comments/1"
]

# Iterar sobre las URLs de las API
for apiUrl in apiUrls:
    # Hacer solicitud GET a la API
    response = requests.get(apiUrl)

    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Imprimir el JSON de la respuesta
        print(f"JSON de {apiUrl}:")
        print(response.json())
        print("\n")

    else:
        print(f"Error al obtener datos de {apiUrl}. Código de estado: {response.status_code}")

````

Este programa de python se conecta a tres API diferentes, obtiene el JSON de cada una y muestra ese JSON junto con los pares de clave-valorm, tal que:

- Se utiliza la biblioteca `requests` para realizar solicitudes HTTP a las API.
- Se define una lista llamada `apiUrls` que contiene las URL de las tres API a las que se conectará.
- Se itera sobre cada URL de la API.
- Se realiza una solicitud GET a cada API y se verifica si la solicitud fue exitosa (código de estado 200).
- Si la solicitud fue exitosa, se imprime el JSON resultante y sus pares de clave-valor.
- Si la solicitud no fue exitosa, se imprime un mensaje de error junto con el código de estado.

Para mejorar el rendimineto, les recomiendo instalar el request, si no saben como, copien y peguen este comando en la terminal:
```python
pip install request
````
Ya con esto, les debería funcionar todo perfectamente.
Agradezco al profesor Felipe Gonzales por la inspiracón que nos dio al grupo, yo creo que por eso no todos cancelaron la materia jaja (En otros grupos de programación terminaron solo 10 personas, entonces el profe Felipe supo dar clase y por eso fue "recompensado" en la encuesta docente jaja)
Y omo es de costumbre, les agradezco por su atención y esperando que se comprenda o se aprenda algo nuevo. ¡Muchas gracias!
