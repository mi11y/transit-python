import atexit
from dateutil import parser
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from Utils.MatrixDisplay import MatrixDisplay
from Trimet.TrimetPresenter import TrimetPresenter
from Utils.DataParser import DataParser

from Biketown.Stations.StationsPresenter import StationsPresenter
from Scooters.ScooterPresenter import ScooterPresenter

class Coordinator:
    def __init__(self):
        self.matrixDisplay = MatrixDisplay(32, 64)
        self.dataParser = DataParser()
        self.dataParser.setLatLon(lat="45.518538", lon="-122.678358")
        self.dataParser.poll()
        self.trimetPresenter = TrimetPresenter(self.dataParser.getData(), self.matrixDisplay, 260)
        self.biketownStationsPresenter = StationsPresenter(self.dataParser.getData(), self.matrixDisplay, 30)
        self.scooterPresenter = ScooterPresenter(self.dataParser.getData(), self.matrixDisplay, 10)

    def clear_screen(self):
        self.matrixDisplay.clear_screen()
    
    def run(self):
        while True:
            self.scooterPresenter.updateFrom(self.dataParser.getData())
            self.scooterPresenter.run()
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

