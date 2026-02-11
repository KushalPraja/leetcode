class RideSharingSystem:
    
    # these are our queues
    def __init__(self):
        self.riders = []
        self.drivers = []

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self):
        if self.riders and self.drivers:
            driver = self.drivers[0]
            rider = self.riders[0]
            self.drivers.pop(0)
            self.riders.pop(0)
            return [driver, rider]
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders:
            self.riders.remove(riderId)
               
