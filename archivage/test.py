import requests


url = 'http://127.0.0.1:8000/file'
file = {'file': open('une_image.png', 'rb')}
resp = requests.put(url=url, files=file) 
print(resp.json())
