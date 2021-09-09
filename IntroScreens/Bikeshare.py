from Utils.TimeKeeperImproved import TimeKeeperImproved

class Bikeshare:
    def __init__(self, matrixDisplay, timeOut):
        self.matrixDisplay  = matrixDisplay
        self.grandTimeOut = TimeKeeperImproved(timeOut = timeOut)

    def run(self):
        self.grandTimeOut.reset()
        self.redraw()
        while (not self.grandTimeOut.isTimedOut()):
            continue
        self.grandTimeOut.reset()

    def redraw(self):
        self.paint_black()
        self.paintMapPin()
        self.drawText()
        self.matrixDisplay.setImage()

    def paintMapPin(self):
        self.matrixDisplay.loadImage(path='Utils/Resources/Bike_logo.png')
        self.matrixDisplay.pasteOnto()
    
    def drawText(self):
        self.matrixDisplay.draw_text(31, 1, "Nearby\nStations")

    def paint_black(self):
        self.matrixDisplay.paint_black()