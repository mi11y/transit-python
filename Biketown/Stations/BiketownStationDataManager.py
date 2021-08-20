class BiketownStationDataManager:
    def __init__(self, parsedJson):
        self.setData(parsedJson)

    def setData(self, parsedJson):
        self.setParsedJson(parsedJson)
        self.currentStation = 0

    def setParsedJson(self, parsedJson):
        print("[BiketownStationDataManager][setParsedJson] updating parsedJson to:")
        print(parsedJson["share_stations"]["biketown"])
        self.parsedJson = parsedJson["share_stations"]["biketown"]

    def stationCount(self):
        return len(self.parsedJson)

    def getCurrentStation(self):
        return self.parsedJson[self.currentStation]

    def nextStation(self):
        self.currentStation = ((self.currentStation + 1) % len(self.parsedJson))
