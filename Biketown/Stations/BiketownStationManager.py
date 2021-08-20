class BiketownStationManager:
    def __init__(self, parsedJson):
        self.parsedJson = parsedJson

    def getStationName(self):
        if self.parsedJson == None:
            return None
        return self.parsedJson["name"]

    def getNumberOfBikes(self):
        if self.parsedJson == None:
            return None
        return self.parsedJson["station_status"]["num_bikes_available"]