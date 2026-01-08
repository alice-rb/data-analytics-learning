import requests
import json
import os

1
BASE_URL = 'https://jsonplaceholder.typicode.com'

'''GET --> Consultar info'''
response = requests.get(f'{BASE_URL}/posts')

if response.status_code == 200:
    print('Solicitud exitosa')
    print(response.json())
else:
    print(f'Error de solicitud: {response.status_code}')

'''POST --> Publicar nueva info'''
data = {
    'title':'new_year',
    'body':'Happy New Year 2026',
    'userId':5
}
response = requests.post(f'{BASE_URL}/posts', json=data)

if response.status_code == 201:
    print('Creación exitosa')
    print(response.json())
else:
    print(f'Error de solicitud: {response.status_code}')

'''PUT --> Actualizar info'''
post_id = 1

updated_post ={
    'title':'Happy Birthday',
    'body': 'Have a Happy 32nd birthday!',
    'userId': 6
}

response = requests.put(f'{BASE_URL}/posts/{post_id}',json=updated_post)

if response.status_code == 200:
    print('Actualización exitosa')
    print(response.json())
else:
    print(f'Error de solicitud: {response.status_code}')

'''PATCH --> Actualizar parcialmente la info'''
post_id = 2

updated_post = {
    'title':'Holidays, yay!'
}

response = requests.patch(f'{BASE_URL}/posts/{post_id}',json=updated_post)

if response.status_code == 200:
    print('Actualización parcial exitosa')
    print(response.json())
else:
    print(f'Error de solicitud: {response.status_code}')

'''DELETE --> Borrar info existente'''
post_id = 1

response = requests.delete(f'{BASE_URL}/posts/{post_id}')

if response.status_code == 200:
    print('Eliminación exitosa')
else:
    print(f'Error de solicitud: {response.status_code}')

#2
URL = 'http://api.openweathermap.org/data/2.5/weather'
KEY = os.getenv('OPENWEATHER_API_KEY')
os.environ["OPENWEATHER_API_KEY"] = '8a11193255404a492eec71ed9d9f66d3'

def climaInfo():
    if not KEY:
        print('Error: No se encontró la clave')

    ciudad = input('Introduce el nombre de la ciudad: ')
    try:
        url = f'{URL}?q={ciudad}&appid={KEY}&units=metric&lang=es'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            desc = data['weather'][0]['description']
            temp = data['main']['temp']

            print(f'Clima en {ciudad} es: {desc}')
            print(f'Temperatura: {temp} grados celsius')
        
        elif response.status_code == 404:
            print(f'Ciudad no válida')
        
        else:
            print(f'Error de solicitud: {response.status_code}')
    
    except requests.exceptions.RequestException as e:
        print(f'Error conexión: {e}')

climaInfo()

