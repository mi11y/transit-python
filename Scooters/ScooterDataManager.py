class ScooterDataManager:
    def __init__(self, parsedJson):
        self.parsedJson = parsedJson

    def setData(self, parsedJson):
        self.parsedJson = parsedJson

    def getSpinScooterCount(self):
        if len(self.parsedJson["bike_shares"]) < 1:
            return 0
        return len(self.parsedJson["bike_shares"]["Spin"])

    def getLimeScooterCount(self):
        if len(self.parsedJson["bike_shares"]) < 1:
            return 0
        return len(self.parsedJson["bike_shares"]["Lime"])

    def getBirdScooterCount(self):
        if len(self.parsedJson["bike_shares"]) < 1:
            return 0
        return len(self.parsedJson["bike_shares"]["Bird"])

    def getBiketownScooterCount(self):
        if len(self.parsedJson["bike_shares"]) < 1:
            return 0
        return len(self.parsedJson["bike_shares"]["Biketown"])

    def getBoltScooterCount(self):
        if len(self.parsedJson["bike_shares"]) < 1:
            return 0
        return len(self.parsedJson["bike_shares"]["Bolt"])