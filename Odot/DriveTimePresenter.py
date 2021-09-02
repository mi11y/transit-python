from Utils.TimeKeeper import TimeKeeper
from Utils.DataParser import DataParser
from Odot.DriveTimeDataManager import DriveTimeDataManager
from Odot.DriveTimeOriginManager import DriveTimeOriginManager

class DriveTimePresenter:
    def __init__(self, parsedData, matrixDisplay, timeOut):
        self.matrixDisplay = matrixDisplay
        self.timeKeeper = TimeKeeper(grandTimeOut=timeOut, swapTimeOut=3)
        self.driveTimeDataManager = DriveTimeDataManager(parsedData)
        self.show_estimates = False


    def updateFrom(self, parsedData):
        self.driveTimeDataManager.setData(parsedData)

    def redraw(self):
        self.paint_black()
        self.draw_highway_signs()
        if(self.show_estimates):
            self.draw_estimates()
        else:
            self.matrixDisplay.draw_horizontal_divder()
            self.draw_cross_streets()
        self.matrixDisplay.setImage()

    def run(self):
        self.timeKeeper.reset_start_time()
        if self.driveTimeDataManager.driveTimeCount() < 1:
            return
        self.driveTimeOriginManager = DriveTimeOriginManager(self.driveTimeDataManager.getCurrentDriveTime())
        self.currentDestination = self.driveTimeOriginManager.getCurrentDestination()
        self.nextDestination = self.driveTimeOriginManager.getNextDestination()
        self.redraw()
        while (not self.timeKeeper.is_timed_out()):
            if(self.timeKeeper.should_swap()):
                self.swap()
                self.redraw()

            if(self.timeKeeper.should_show_next_route()):
                print("Next Destination!")
                self.timeKeeper.reset_next_route_prev_time()
                self.paint_black()
                self.driveTimeOriginManager.updateCurrentDestination()
                self.currentDestination = self.driveTimeOriginManager.getCurrentDestination()
                self.nextDestination = self.driveTimeOriginManager.getNextDestination()
                self.redraw()

            if(self.timeKeeper.should_show_next_stop()):
                print("Next Origin!")
                self.timeKeeper.reset_next_route_prev_time()
                self.timeKeeper.reset_swap_prev_time()
                self.timeKeeper.reset_next_stop_prev_time()
                self.paint_black()
                self.driveTimeDataManager.nextDriveTime()
                self.driveTimeOriginManager = DriveTimeOriginManager(self.driveTimeDataManager.getCurrentDriveTime())
                self.currentDestination = self.driveTimeOriginManager.getCurrentDestination()
                self.nextDestination = self.driveTimeOriginManager.getNextDestination()
                self.redraw()

        self.timeKeeper.reset_start_time()

    def swap(self):
        print("Swap!")
        self.show_estimates = not self.show_estimates
        print("show estimates? ")
        print(self.show_estimates)
        self.timeKeeper.reset_swap_prev_time()
        self.paint_black()

    def paint_black(self):
        self.matrixDisplay.paint_black()

    def draw_data(self):
        self.drawBackground()
        self.drawHighwaySign()

    def drawBackground(self):
        self.matrixDisplay.paint_solid_color_background(fill="#000")

    def draw_highway_signs(self):
        if self.driveTimeOriginManager.isInterstateHighway():
            self.matrixDisplay.draw_interstate_highway_sign(1, 3, 10, 10, self.driveTimeOriginManager.getLocationName())

        if self.driveTimeOriginManager.isOregonHighway():
            self.matrixDisplay.draw_oregon_highway_sign(1, 3, 10, 10, self.driveTimeOriginManager.getLocationName())

        if self.currentDestination.isInterstateHighway():
            self.matrixDisplay.draw_interstate_highway_sign(1, 19, 10, 10, self.currentDestination.getLocationName())

        if self.currentDestination.isOregonHighway():
            self.matrixDisplay.draw_oregon_highway_sign(1, 19, 10, 10, self.currentDestination.getLocationName())

        if self.currentDestination.isWashingtonHighway():
            self.matrixDisplay.draw_state_route_sign(1, 19, 10, 10, self.currentDestination.getLocationName())

    def draw_cross_streets(self):
        self.matrixDisplay.draw_arrival(13, -1, self.driveTimeOriginManager.getCrossStreet())
        if self.currentDestination.isRoad():
            self.matrixDisplay.draw_arrival(1, 15, self.currentDestination.getCrossStreet())
        else:
            self.matrixDisplay.draw_arrival(13, 15, self.currentDestination.getCrossStreet())

    def draw_estimates(self):
        self.matrixDisplay.draw_text(13, 10, str(self.currentDestination.getTravelTime()) + " MIN")