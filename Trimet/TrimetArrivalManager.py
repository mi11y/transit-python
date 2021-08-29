class TrimetArrivalManager:
    def __init__(self, parsedJson):
        self.parsedJson = parsedJson

    def get_route_number(self):
        if self.hasRailShortSign():
            return self.getRailShortSign()
        elif self.hasRouteColor():
            return "M"
        else:
            return str(self.getArrivalRoute())

    def getArrivalRoute(self):
        return self.parsedJson["route"]
    
    def getArrivalScheduled(self):
        return self.parsedJson["scheduled"]
    
    def getArrivalFullSign(self):
        return self.parsedJson["full_sign"]
    
    def getArrivalShortSign(self):
        return self.parsedJson["short_sign"]
    
    def hasRouteColor(self):
        return "route_color" in self.parsedJson["route_info"]

    def hasRailShortSign(self):
        return "rail_short_sign" in self.parsedJson["route_info"]

    def getRailShortSign(self):
        return self.parsedJson["route_info"]["rail_short_sign"]

    def getArrivalRouteColor(self):
        return self.parsedJson["route_info"]["route_color"]
    
    def getArrivalDesc(self):
        return self.parsedJson["desc"]

    def isFrequentService(self):
         return self.parsedJson["route_info"]["frequent_service"]
