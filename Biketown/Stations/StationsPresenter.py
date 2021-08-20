from Utils.TimeKeeper import TimeKeeper
from Utils.DataParser import DataParser
from Biketown.Stations.BiketownStationDataManager import BiketownStationDataManager
from Biketown.Stations.BiketownStationManager import BiketownStationManager

class StationsPresenter:
    def __init__(self, parsedData, matrixDisplay, timeOut):
        self.matrixDisplay  = matrixDisplay
        self.timeKeeper = TimeKeeper(grandTimeOut=timeOut, swapTimeOut=3)

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
        self.timeKeeper.reset_start_time()
        if self.biketownStationDataManager.stationCount() == 0:
            return

        self.biketownStationManager = BiketownStationManager(self.biketownStationDataManager.getCurrentStation())

        self.redraw()
        while (not self.timeKeeper.is_timed_out()):
            if(self.timeKeeper.should_show_next_route()):
                print("Next Station!")
                self.timeKeeper.reset_next_route_prev_time()
                self.timeKeeper.reset_swap_prev_time()
                self.paint_black()
                self.biketownStationDataManager.nextStation()
                self.biketownStationManager = BiketownStationManager(self.biketownStationDataManager.getCurrentStation())
                self.redraw()
        self.timeKeeper.reset_start_time()


    def paint_black(self):
        self.matrixDisplay.paint_black()

    def draw_biketown_logo(self):
        self.matrixDisplay.draw_text(1, 18, "Biketown", "#b33f25")

    def draw_num_bikes_available(self):
        self.matrixDisplay.draw_text(52, 18, str(self.biketownStationManager.getNumberOfBikes()))

    def draw_station_name(self):
        self.matrixDisplay.draw_arrival(1, -1, str(self.biketownStationManager.getStationName()))
