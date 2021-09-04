import time

class TimeKeeperImproved:
    def __init__(self, timeOut=64):
        self.timeOut = timeOut
        self.startTime = time.time()
    
    def reset(self):
        self.startTime = time.time()
    
    def isTimedOut(self):
        return (time.time() - self.startTime) > self.timeOut
