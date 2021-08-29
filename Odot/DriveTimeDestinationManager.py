class DriveTimeDestinationManager:
    def __init__(self, parsedJson):
        self.parsedJson = parsedJson

    def getRouteDestination(self):
        return self.parsedJson["route_destination"]

    def getMinimumRouteTime(self):
        return self.parsedJson["min_route_time"]
    def getTravelTime(self):
        return self.parsedJson["travel_time"]

    def getLocationName(self):
        return self.parsedJson["route_destination"]

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
        if self.isRoad():
            return self.getLocationName()
        return self.parsedJson["cross_street"]

    def getDirection(self):
        return self.parsedJson["direction"]

    def getDelay(self):
        return self.parsedJson["delay"]
