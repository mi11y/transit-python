class TrimetDataManager:
    def __init__(self, parsedJson):
        self.setData(parsedJson)

    def setData(self, parsedJson):
        self.setParsedJson(parsedJson)
        self.currentStop = 0
        self.keysList = list(self.stops().keys())
    
    def setParsedJson(self, parsedJson):
        print("[TrimetDataManager][setParsedJson] updating parsedJson to:")
        print(parsedJson)
        self.parsedJson = parsedJson

    def stopCount(self):
        return len(self.parsedJson["trimet_stops"])
    
    def getCurrentStop(self):
        print("[TrimetDataManager][getCurrentStop]::")
        print(self.indexToKey())
        return self.stops()[self.indexToKey()]
    
    def nextStop(self):
        self.currentStop = ((self.currentStop + 1) % len(self.keysList))

    def stops(self):
        return self.parsedJson["trimet_stops"]
    
    def indexToKey(self):
        return self.keysList[self.currentStop]
