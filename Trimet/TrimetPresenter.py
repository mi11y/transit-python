from Utils.TimeKeeper import TimeKeeper
from Utils.DataParser import DataParser
from Trimet.TrimetDataManager import TrimetDataManager
from Trimet.TrimetStopManager import TrimetStopManager

class TrimetPresenter:
    def __init__(self, parsedData, matrixDisplay, timeOut):
        self.matrixDisplay  = matrixDisplay
        self.timeKeeper = TimeKeeper(grandTimeOut=timeOut, swapTimeOut=3)
        self.show_estimates = False
        self.trimetDataManager = TrimetDataManager(parsedData)

    def updateFrom(self, parsedData):
        self.trimetDataManager.setData(parsedData)
    
    def redraw(self):
        self.paint_black()
        self.draw_route_signs()

        if(self.show_estimates):
            self.draw_estimates()
            self.draw_direction()
        else:
            self.draw_street()

        self.matrixDisplay.setImage()


    def run(self):
        self.timeKeeper.reset_start_time()

        if self.trimetDataManager.stopCount() < 1:
            return

        self.trimetStopManager = TrimetStopManager(self.trimetDataManager.getCurrentStop())
        self.currentArrival = self.trimetStopManager.getCurrentArrival()
        self.nextArrival = self.trimetStopManager.getNextArrival()

        self.redraw()
        while (not self.timeKeeper.is_timed_out()):
            if(self.timeKeeper.should_swap()):
                self.swap()
                self.redraw()

            if(self.timeKeeper.should_show_next_route()):
                print("Next route!")
                self.timeKeeper.reset_next_route_prev_time()
                self.timeKeeper.reset_swap_prev_time()
                self.paint_black()
                self.trimetStopManager.updateCurrentArrival()
                self.currentArrival = self.trimetStopManager.getCurrentArrival()
                self.nextArrival = self.trimetStopManager.getNextArrival()
                self.redraw()

            if(self.timeKeeper.should_show_next_stop()):
                print("Next Stop!")
                self.timeKeeper.reset_next_route_prev_time()
                self.timeKeeper.reset_swap_prev_time()
                self.timeKeeper.reset_next_stop_prev_time()
                self.paint_black()
                self.trimetDataManager.nextStop()
                self.trimetStopManager = TrimetStopManager(self.trimetDataManager.getCurrentStop())
                self.currentArrival = self.trimetStopManager.getCurrentArrival()
                self.nextArrival = self.trimetStopManager.getNextArrival()
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

    def draw_street(self):
        self.matrixDisplay.draw_arrival(13, -1, self.trimetStopManager.getStopDescription())
        self.matrixDisplay.draw_arrival(13, 15, self.trimetStopManager.getStopDescription())

    def draw_estimates(self):
        self.matrixDisplay.draw_estimate(13, -1, self.currentArrival.getArrivalScheduled())
        self.matrixDisplay.draw_estimate(13, 15, self.nextArrival.getArrivalScheduled())
    
    def draw_direction(self):
        self.matrixDisplay.draw_text(14, 6, self.trimetStopManager.getStopDir())
        self.matrixDisplay.draw_text(14, 22, self.trimetStopManager.getStopDir())

    def draw_route_signs(self):
        topRouteColor    = self.currentArrival.getArrivalRouteColor() if self.currentArrival.hasRouteColor() else "#042340"
        bottomRouteColor = self.nextArrival.getArrivalRouteColor() if self.nextArrival.hasRouteColor() else "#042340"

        self.matrixDisplay.draw_horizontal_divder()
        self.matrixDisplay.draw_route_sign(1, 1, 12, 12, str(self.currentArrival.get_route_number()), topRouteColor, "#000")
        self.matrixDisplay.draw_route_sign(1, 18, 12, 12, str(self.nextArrival.get_route_number()),   bottomRouteColor, "#000")

