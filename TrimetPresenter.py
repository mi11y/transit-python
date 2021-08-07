from TimeKeeper import TimeKeeper

class TrimetPresenter:
    def __init__(self, matrixDisplay, timeOut):
        self.matrixDisplay  = matrixDisplay
        self.timeKeeper = TimeKeeper(grandTimeOut=timeOut, swapTimeOut=3)
        self.show_estimates = False

    def run(self):
        while (not self.timeKeeper.is_timed_out()):
            self.matrixDisplay.setImage()
            self.draw_route_signs()

            if(self.timeKeeper.should_swap()):
                self.swap()

            if(self.show_estimates):
                self.draw_estimates()
            else:
                self.draw_street()

            if(self.timeKeeper.should_show_next_route()):
                print("Next route!")
                self.timeKeeper.reset_next_route_prev_time()
                self.timeKeeper.reset_swap_prev_time()

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
        self.matrixDisplay.draw_arrival(14, -1, "SW 5th & Morrison")
        self.matrixDisplay.draw_arrival(14, 15, "SW 6th & Yamhill")

    def draw_estimates(self):
        self.matrixDisplay.draw_estimate(14, -1, "2021-08-06T06:25:00+00:00")
        self.matrixDisplay.draw_estimate(14, 15, "2021-08-06T06:46:00+00:00")

    def draw_route_signs(self):
        self.matrixDisplay.draw_horizontal_divder()
        self.matrixDisplay.draw_route_sign(2, 2, 12, 12, "8", "#042340", "#000")
        self.matrixDisplay.draw_route_sign(2, 18, 12, 12, "12", "#042340", "#000")
