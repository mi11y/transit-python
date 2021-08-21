import time

class TimeKeeper:
    def __init__(self, grandTimeOut=256, swapTimeOut=4, nextRouteTimeOut=8, nextStopTimeOut=32):
        self.swapTimeOut = swapTimeOut
        self.grandTimeOut = grandTimeOut
        self.nextRouteTimeOut = nextRouteTimeOut
        self.nextStopTimeOut = nextStopTimeOut
        self.start_time = time.time()
        self.swap_prev_time = time.time()
        self.next_route_prev_time = time.time()
        self.next_stop_prev_time = time.time()

    def reset_swap_prev_time(self):
        self.swap_prev_time = time.time()

    def reset_next_route_prev_time(self):
        self.next_route_prev_time = time.time()
    
    def reset_next_stop_prev_time(self):
        self.next_stop_prev_time = time.time()
    
    def reset_start_time(self):
        self.start_time = time.time()
    
    def reset_all(self):
        self.timeKeeper.reset_swap_prev_time()
        self.timeKeeper.reset_next_route_prev_time()
        self.timeKeeper.reset_next_stop_prev_time()
        self.reset_start_time()
    
    def is_timed_out(self):
        if(self.grandTimeOut <= 0):
            return False
        return (time.time() - self.start_time) > self.grandTimeOut

    def should_show_next_route(self):
        return (time.time() - self.next_route_prev_time) > self.nextRouteTimeOut

    def should_show_next_stop(self):
        return (time.time() - self.next_stop_prev_time) > self.nextStopTimeOut

    def should_swap(self):
        return (time.time() - self.swap_prev_time) > self.swapTimeOut
