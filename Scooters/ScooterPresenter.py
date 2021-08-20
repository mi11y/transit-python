from Utils.TimeKeeper import TimeKeeper
from Utils.DataParser import DataParser
from Scooters.ScooterDataManager import ScooterDataManager

class ScooterPresenter:
    def __init__(self, parsedData, matrixDisplay, timeOut):
        self.matrixDisplay  = matrixDisplay
        self.timeKeeper = TimeKeeper(grandTimeOut=timeOut, swapTimeOut=3)
        self.show_estimates = False
        self.scooterDataManager = ScooterDataManager(parsedData)


    def updateFrom(self, parsedData):
        self.scooterDataManager.setData(parsedData)

    def redraw(self):
        self.paint_black()
        self.draw_data()
        self.matrixDisplay.setImage()

    def run(self):
        self.timeKeeper.reset_start_time()
        self.redraw()
        while (not self.timeKeeper.is_timed_out()):
            continue
        self.timeKeeper.reset_start_time()

    def paint_black(self):
        self.matrixDisplay.paint_black()

    def draw_data(self):
        self.drawBiketown()
        self.drawLime()
        self.drawBird()
        self.drawSpin()

    def drawBiketown(self):
        self.matrixDisplay.draw_text(1, -2, "Biketown", "#b33f25")
        self.matrixDisplay.draw_text(52, -2, str(self.scooterDataManager.getBiketownScooterCount()))

    def drawLime(self):
        self.matrixDisplay.draw_text(1, 6, "Lime", "#1a9e00")
        self.matrixDisplay.draw_text(52, 6, str(self.scooterDataManager.getLimeScooterCount()))

    def drawBird(self):
        self.matrixDisplay.draw_text(1, 14, "Bird", "#6b6b6b")
        self.matrixDisplay.draw_text(52, 14, str(self.scooterDataManager.getBirdScooterCount()))

    def drawSpin(self):
        self.matrixDisplay.draw_text(1, 22, "Spin", "#11769e")
        self.matrixDisplay.draw_text(52, 22, str(self.scooterDataManager.getSpinScooterCount()))
