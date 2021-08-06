import requests
r = requests.get('http://192.168.1.132:5000/locations/show')
print("r.status code=")
print(r.status_code)
print(r.json())