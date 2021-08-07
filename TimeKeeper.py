import time

class TimeKeeper:
    def __init__(self, grandTimeOut=120, swapTimeOut=3, nextRouteTimeOut=18):
        self.swapTimeOut = swapTimeOut
        self.grandTimeOut = grandTimeOut
        self.nextRouteTimeOut = nextRouteTimeOut
        self.start_time = time.time()
        self.swap_prev_time = time.time()
        self.next_route_prev_time = time.time()

    def reset_swap_prev_time(self):
        self.swap_prev_time = time.time()

    def reset_next_route_prev_time(self):
        self.next_route_prev_time = time.time()
    
    def is_timed_out(self):
        return (time.time() - self.start_time) > self.grandTimeOut

    def should_show_next_route(self):
        return (time.time() - self.next_route_prev_time) > self.nextRouteTimeOut

    def should_swap(self):
        return (time.time() - self.swap_prev_time) > self.swapTimeOut
