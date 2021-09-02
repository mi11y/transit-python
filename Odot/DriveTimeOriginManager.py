from Odot.DriveTimeDestinationManager import DriveTimeDestinationManager

class DriveTimeOriginManager:
    def __init__(self, parsedJson):
        self.parsedJson = parsedJson
        self.currentDestination = 0

    def getCurrentDestination(self):
        return DriveTimeDestinationManager(self.destinations()[self.currentDestination])

    def getNextDestination(self):
        return DriveTimeDestinationManager(self.destinations()[self.nextDestination()])

    def getLocationName(self):
        return self.parsedJson["location_name"]
    def getHighwayType(self):
        return self.parsedJson["highway_type"]
    def isInterstateHighway(self):
        return self.getHighwayType() == "Interstate"
    def isUSHighway(self):
        return self.getHighwayType() == "US"
    def isOregonHighway(self):
        return self.getHighwayType() == "Oregon"
    def isWashingtonHighway(self):
        return self.getHighwayType() == "SR"
    def isRoad(self):
        return self.getHighwayType() == "Road"
    def getCrossStreet(self):
        return self.parsedJson["cross_street"]
    def getDirection(self):
        return self.parsedJson["direction"]

    def updateCurrentDestination(self):
        self.currentDestination = self.nextDestination()

    def nextDestination(self):
        return ((self.currentDestination + 1) % len(self.destinations()))

    def destinations(self):
        return self.parsedJson["destinations"]