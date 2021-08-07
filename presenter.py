import atexit
from dateutil import parser
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from MatrixDisplay import MatrixDisplay
from TrimetPresenter import TrimetPresenter
from DataParser import DataParser

class Coordinator:
    def __init__(self):
        self.matrixDisplay = MatrixDisplay(32, 64)
        self.dataParser = DataParser()
        self.dataParser.setLatLon(lat="45.534032", lon="-122.695187")
        self.dataParser.poll()
        self.trimetPresenter = TrimetPresenter(self.dataParser.getData(), self.matrixDisplay, 120)

    def clear_screen(self):
        self.matrixDisplay.clear_screen()
    
    def run(self):
        while True:
            self.trimetPresenter.updateFrom(self.dataParser.getData())
            self.trimetPresenter.run()
            self.dataParser.poll()

presenter = Coordinator()


def clearOnExit():
    presenter.clear_screen()
atexit.register(clearOnExit)

presenter.run()

