from Utils.TimeKeeperImproved import TimeKeeperImproved
from Utils.DataParser import DataParser
from Biketown.Stations.BiketownStationDataManager import BiketownStationDataManager
from Biketown.Stations.BiketownStationManager import BiketownStationManager

class StationsPresenter:
    def __init__(self, parsedData, matrixDisplay, timeOut):
        self.matrixDisplay  = matrixDisplay
        self.grandTimeOut = TimeKeeperImproved(timeOut = timeOut)
        self.nextRouteTimeOut = TimeKeeperImproved(timeOut = 8)
        self.biketownStationDataManager = BiketownStationDataManager(parsedData)

    def updateFrom(self, parsedData):
        self.biketownStationDataManager.setData(parsedData)

    def redraw(self):
        self.paint_black()
        self.draw_biketown_logo()
        self.draw_station_name()
        self.draw_num_bikes_available()

        self.matrixDisplay.setImage()

    def run(self):
        self.grandTimeOut.reset()
        self.nextRouteTimeOut.reset()

        if self.biketownStationDataManager.stationCount() == 0:
            return

        self.biketownStationManager = BiketownStationManager(self.biketownStationDataManager.getCurrentStation())
        self.redraw()
        
        while (not self.grandTimeOut.isTimedOut()):
            if(self.nextRouteTimeOut.isTimedOut()):
                print("Next Station!")
                self.nextRouteTimeOut.reset()
                self.paint_black()
                self.biketownStationDataManager.nextStation()
                self.biketownStationManager = BiketownStationManager(self.biketownStationDataManager.getCurrentStation())
                self.redraw()
        self.grandTimeOut.reset()
        self.nextRouteTimeOut.reset()

    def paint_black(self):
        self.matrixDisplay.paint_black()

    def draw_biketown_logo(self):
        self.matrixDisplay.loadImage(path='Utils/Resources/Biketown_logo.png')
        self.matrixDisplay.pasteOnto()

    def draw_num_bikes_available(self):
        self.matrixDisplay.draw_text(52, 19, str(self.biketownStationManager.getNumberOfBikes()))

    def draw_station_name(self):
        self.matrixDisplay.draw_arrival(1, 12, str(self.biketownStationManager.getStationName()))
