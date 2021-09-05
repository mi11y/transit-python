from Utils.TimeKeeperImproved import TimeKeeperImproved
from Scooters.ScooterDataManager import ScooterDataManager

class SpinPresenter:
    def __init__(self, parsedData, matrixDisplay, timeOut):
        self.matrixDisplay  = matrixDisplay
        self.grandTimeOut = TimeKeeperImproved(timeOut = timeOut)
        self.scooterDataManager = ScooterDataManager(parsedData)
    
    def updateFrom(self, parsedData):
        self.scooterDataManager.setData(parsedData)

    def run(self):
        self.grandTimeOut.reset()
        self.redraw()
        while (not self.grandTimeOut.isTimedOut()):
            continue
        self.grandTimeOut.reset()

    def redraw(self):
        self.paint_black()
        self.painLogo()
        self.drawText()
        self.matrixDisplay.setImage()
    
    def painLogo(self):
        self.matrixDisplay.loadImage(path='Utils/Resources/Spin_logo.png')
        self.matrixDisplay.pasteOnto()
    
    def drawText(self):
        self.matrixDisplay.draw_text(1, 18, "Nearby")
        self.matrixDisplay.draw_text(50, 18, str(self.scooterDataManager.getSpinScooterCount()))

    def paint_black(self):
        self.matrixDisplay.paint_black()