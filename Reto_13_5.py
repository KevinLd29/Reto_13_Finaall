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
