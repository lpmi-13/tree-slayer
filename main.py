import requests

BASE_URL = 'https://amazing_api.com/'

response = requests.get(BASE_URL).json()

print(response)
