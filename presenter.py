import atexit
from dateutil import parser
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from MatrixDisplay import MatrixDisplay
from TrimetPresenter import TrimetPresenter

class Coordinator:
    def __init__(self):
        self.matrixDisplay = MatrixDisplay(32, 64)
        self.trimetPresenter = TrimetPresenter(self.matrixDisplay, 120)

    def clear_screen(self):
        self.matrixDisplay.clear_screen()
    
    def run(self):
        self.trimetPresenter.run()

presenter = Coordinator()


def clearOnExit():
    presenter.clear_screen()
atexit.register(clearOnExit)

presenter.run()

