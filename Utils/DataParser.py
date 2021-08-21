import json
import requests

class DataParser:
    def __init__(self):
        self.apiUrl = "http://192.168.1.103:5000/locations/show"
        self.lat = "45.518538"
        self.lon = "-122.678358"
        self.parsedJson = {}
    
    def setLatLon(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
    def poll(self):
        print("[DataParser][getData] polling for data....")
        payload = { 'lat': self.lat, 'lon': self.lon }
        response = requests.get(self.apiUrl, params=payload)

        if response.status_code != 200:
            print("[DataParser][getData] status_code=")
            print(response.status_code)
            exit()

        self.parsedJson = json.loads(response.text)
        print("[DataParser][getData] success!")


    def getData(self):
        return self.parsedJson
