class BiketownStationManager:
    def __init__(self, parsedJson):
        self.parsedJson = parsedJson

    def getStationName(self):
        return self.parsedJson["name"]

    def getNumberOfBikes(self):
        return self.parsedJson["station_status"]["num_bikes_available"]