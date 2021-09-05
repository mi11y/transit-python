import atexit
from dateutil import parser
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from Utils.MatrixDisplay import MatrixDisplay
from Trimet.TrimetPresenter import TrimetPresenter
from Utils.DataParser import DataParser

from Biketown.Stations.StationsPresenter import StationsPresenter
from Scooters.SpinPresenter import SpinPresenter
from Scooters.BirdPresenter import BirdPresenter
from Scooters.LimePresenter import LimePresenter
from Scooters.BoltPresenter import BoltPresenter
from Scooters.BiketownPresenter import BiketownPresenter

from IntroScreens.Scooters.Nearby import Nearby

from Odot.DriveTimePresenter import DriveTimePresenter

class Coordinator:
    def __init__(self):
        self.matrixDisplay = MatrixDisplay(32, 64)
        self.dataParser = DataParser()
        self.dataParser.setLatLon(lat="45.518538", lon="-122.678358")
        self.dataParser.poll()
        self.nearbyScootersIntro = Nearby(self.matrixDisplay, 10)
        self.trimetPresenter = TrimetPresenter(self.dataParser.getData(), self.matrixDisplay, 260)
        self.biketownStationsPresenter = StationsPresenter(self.dataParser.getData(), self.matrixDisplay, 30)
        self.spinPresenter = SpinPresenter(self.dataParser.getData(), self.matrixDisplay, 5)
        self.birdPresenter = BirdPresenter(self.dataParser.getData(), self.matrixDisplay, 5)
        self.limePresenter = LimePresenter(self.dataParser.getData(), self.matrixDisplay, 5)
        self.boltPresenter = BoltPresenter(self.dataParser.getData(), self.matrixDisplay, 5)
        self.biketownPresenter = BiketownPresenter(self.dataParser.getData(), self.matrixDisplay, 5)
        self.driveTimePresenter = DriveTimePresenter(self.dataParser.getData(), self.matrixDisplay, 120)

    def clear_screen(self):
        self.matrixDisplay.clear_screen()
    
    def run(self):
        while True:
            self.nearbyScootersIntro.run()
            self.spinPresenter.updateFrom(self.dataParser.getData())
            self.spinPresenter.run()
            self.birdPresenter.updateFrom(self.dataParser.getData())
            self.birdPresenter.run()
            self.limePresenter.updateFrom(self.dataParser.getData())
            self.limePresenter.run()
            self.boltPresenter.updateFrom(self.dataParser.getData())
            self.boltPresenter.run()
            self.biketownPresenter.updateFrom(self.dataParser.getData())
            self.biketownPresenter.run()
            self.biketownStationsPresenter.updateFrom(self.dataParser.getData())
            self.biketownStationsPresenter.run()
            self.trimetPresenter.updateFrom(self.dataParser.getData())
            self.trimetPresenter.run()
            self.driveTimePresenter.updateFrom(self.dataParser.getData())
            self.driveTimePresenter.run()
            self.dataParser.poll()

presenter = Coordinator()


def clearOnExit():
    presenter.clear_screen()
atexit.register(clearOnExit)

presenter.run()

