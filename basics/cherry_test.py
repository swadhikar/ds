import requests

url = 'http://localhost:8080/'
session = requests.Session()

response = session.get(url)

print(response.status_code)
