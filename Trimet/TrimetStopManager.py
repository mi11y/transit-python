from Trimet.TrimetArrivalManager import TrimetArrivalManager

class TrimetStopManager:
    def __init__(self, parsedJson):
        self.parsedJson = parsedJson
        self.currentArrival = 0

    def getCurrentArrival(self):
        return TrimetArrivalManager(self.arrivals()[self.currentArrival])
    
    def getNextArrival(self):
        return TrimetArrivalManager(self.arrivals()[self.nextArrival()])
    
    def getStopDescription(self):
        return self.parsedJson["desc"]
    
    def getStopDir(self):
        return self.parsedJson["dir"]
    
    def updateCurrentArrival(self):
        self.currentArrival = self.nextArrival()

    def nextArrival(self):
        return ((self.currentArrival + 1) % len(self.arrivals()))

    def arrivals(self):
        return self.parsedJson["arrivals"]