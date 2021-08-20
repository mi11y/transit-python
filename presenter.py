import atexit
from dateutil import parser
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from Utils.MatrixDisplay import MatrixDisplay
from Trimet.TrimetPresenter import TrimetPresenter
from Utils.DataParser import DataParser

from Biketown.Stations.StationsPresenter import StationsPresenter

class Coordinator:
    def __init__(self):
        self.matrixDisplay = MatrixDisplay(32, 64)
        self.dataParser = DataParser()
        self.dataParser.setLatLon(lat="45.534032", lon="-122.695187")
        self.dataParser.poll()
        self.trimetPresenter = TrimetPresenter(self.dataParser.getData(), self.matrixDisplay, 240)
        self.biketownStationsPresenter = StationsPresenter(self.dataParser.getData(), self.matrixDisplay, 30)

    def clear_screen(self):
        self.matrixDisplay.clear_screen()
    
    def run(self):
        while True:
            self.biketownStationsPresenter.updateFrom(self.dataParser.getData())
            self.biketownStationsPresenter.run()
            self.trimetPresenter.updateFrom(self.dataParser.getData())
            self.trimetPresenter.run()
            self.dataParser.poll()

presenter = Coordinator()


def clearOnExit():
    presenter.clear_screen()
atexit.register(clearOnExit)

presenter.run()

