from Utils.TimeKeeperImproved import TimeKeeperImproved
from Utils.DataParser import DataParser
from Trimet.TrimetDataManager import TrimetDataManager
from Trimet.TrimetStopManager import TrimetStopManager
from Trimet.ScrollingTimingDefaults import ScrollingTimingDefaults
from Trimet.TimingDefaults import TimingDefaults
from colour import Color

class TrimetPresenter:
    def __init__(self, parsedData, matrixDisplay, timeOut):
        self.matrixDisplay  = matrixDisplay
        self.timingDefinitions = ScrollingTimingDefaults()
        self.grandTimeOut = TimeKeeperImproved(timeOut = timeOut)
        self.swapTimeOut = TimeKeeperImproved(timeOut = self.timingDefinitions.swapTimeOut)
        self.showNextRoute = TimeKeeperImproved(timeOut = self.timingDefinitions.showNextRoute)
        self.showNextStop = TimeKeeperImproved(timeOut = self.timingDefinitions.showNextStop)
        self.scrollLeftTimeOut = TimeKeeperImproved(timeOut = self.timingDefinitions.scrollLeftTimeOut)
        self.show_estimates = False
        self.drawAtX = 60
        self.trimetDataManager = TrimetDataManager(parsedData)

    def updateFrom(self, parsedData):
        self.trimetDataManager.setData(parsedData)
    
    def scrollLeft(self):
        self.drawAtX = self.drawAtX - 1
        if self.drawAtX < -64:
            self.drawAtX = 64

    def redraw(self):
        self.drawPresentation()
        self.matrixDisplay.setImageDoubleBuffer()
        self.scrollLeft()

        self.paint_black()
        self.drawPresentation()
        self.matrixDisplay.setImageDoubleBuffer()

        self.matrixDisplay.doubleBufferDraw()

    def drawPresentation(self):
        if(self.show_estimates):
            self.draw_estimates()
            self.draw_direction()
        else:
            self.draw_street()
        self.draw_route_signs()

    def run(self):
        self.grandTimeOut.reset()
        self.swapTimeOut.reset()
        self.showNextRoute.reset()
        self.showNextStop.reset()
        self.scrollLeftTimeOut.reset()

        if self.trimetDataManager.stopCount() < 1:
            return

        self.trimetStopManager = TrimetStopManager(self.trimetDataManager.getCurrentStop())
        self.currentArrival = self.trimetStopManager.getCurrentArrival()
        self.nextArrival = self.trimetStopManager.getNextArrival()

        self.redraw()
        while (not self.grandTimeOut.isTimedOut()):
            if(self.swapTimeOut.isTimedOut()):
                self.swap()

            if(self.showNextRoute.isTimedOut()):
                print("Next route!")
                self.showNextRoute.reset()
                self.swapTimeOut.reset()
                self.show_estimates = False
                self.paint_black()
                self.trimetStopManager.updateCurrentArrival()
                self.currentArrival = self.trimetStopManager.getCurrentArrival()
                self.nextArrival = self.trimetStopManager.getNextArrival()

            if(self.showNextStop.isTimedOut()):
                print("Next Stop!")
                self.showNextRoute.reset()
                self.swapTimeOut.reset()
                self.showNextStop.reset()
                self.paint_black()
                self.trimetDataManager.nextStop()
                self.trimetStopManager = TrimetStopManager(self.trimetDataManager.getCurrentStop())
                self.currentArrival = self.trimetStopManager.getCurrentArrival()
                self.nextArrival = self.trimetStopManager.getNextArrival()
            
            self.redraw()
            
        self.grandTimeOut.reset()
        self.swapTimeOut.reset()
        self.showNextRoute.reset()
        self.showNextStop.reset()
        self.scrollLeftTimeOut.reset()

    def swap(self):
        print("Swap!")
        self.show_estimates = not self.show_estimates
        print("show estimates? ")
        print(self.show_estimates)
        self.swapTimeOut.reset()
        self.paint_black()

    def paint_black(self):
        self.matrixDisplay.paint_black()

    def draw_street(self):
        self.matrixDisplay.draw_arrival(self.drawAtX, -1, self.trimetStopManager.getStopDescription())
        self.matrixDisplay.draw_arrival(self.drawAtX, 15, self.trimetStopManager.getStopDescription())

    def draw_estimates(self):
        self.matrixDisplay.draw_estimate(self.drawAtX, -1, self.currentArrival.getArrivalScheduled())
        self.matrixDisplay.draw_estimate(self.drawAtX, 15, self.nextArrival.getArrivalScheduled())
    
    def draw_direction(self):
        self.matrixDisplay.draw_text(self.drawAtX, 6, self.trimetStopManager.getStopDir())
        self.matrixDisplay.draw_text(self.drawAtX, 22, self.trimetStopManager.getStopDir())

    def draw_route_signs(self):
        topRouteColor    = self.currentArrival.getArrivalRouteColor() if self.currentArrival.hasRouteColor() else "#0c5ca7"
        bottomRouteColor = self.nextArrival.getArrivalRouteColor() if self.nextArrival.hasRouteColor() else "#0c5ca7"
        topRouteColor = Color(topRouteColor)
        bottomRouteColor = Color(bottomRouteColor)
        # if topRouteColor.luminance > 0.40:
        #     topRouteColor.luminance = 0.40
        # if bottomRouteColor.luminance > 0.40:
        #     bottomRouteColor.luminance = 0.40
        self.matrixDisplay.drawRectangle(0, 0, 14, 32, "#000")
        self.matrixDisplay.draw_horizontal_divder()
        self.matrixDisplay.draw_route_sign(1, 1, 12, 12, str(self.currentArrival.get_route_number()), topRouteColor.hex, "#000")
        self.matrixDisplay.draw_route_sign(1, 18, 12, 12, str(self.nextArrival.get_route_number()),   bottomRouteColor.hex, "#000")

        if self.currentArrival.isFrequentService():
            self.matrixDisplay.draw_route_border(0,0,0,0, "#3b990f")
        if self.nextArrival.isFrequentService():
            self.matrixDisplay.draw_route_border(0,17,0,0, "#3b990f")
