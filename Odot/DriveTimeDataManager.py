class DriveTimeDataManager:
    def __init__(self, parsedJson):
        self.setData(parsedJson)

    def setData(self, parsedJson):
        self.setParsedJson(parsedJson)
        self.currentDriveTime = 0

    def setParsedJson(self, parsedJson):
        print("[DriveTimeDataManager][setParsedJson] updating parsedJson to:")
        print(parsedJson)
        self.parsedJson = parsedJson

    def driveTimeCount(self):
        return len(self.driveTimes())

    def getCurrentDriveTime(self):
        print("[DriveTimeDataManager][getCurrentStop]::")
        print(self.driveTimes()[self.currentDriveTime])
        return self.driveTimes()[self.currentDriveTime]

    def nextDriveTime(self):
        self.currentDriveTime = ((self.currentDriveTime + 1) % self.driveTimeCount())

    def driveTimes(self):
        return self.parsedJson["drive_times"]