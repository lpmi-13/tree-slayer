import requests
import os

SECRET_API_KEY = os.getenv('SECRET_API_KEY')

BASE_URL = 'https://amazing_api.com'

headers = {
    'content-type': 'application/json',
    'Authorization': f'Bearer {SECRET_API_KEY}'
}

response = requests.get(BASE_URL, headers=headers).json()

print(response)
