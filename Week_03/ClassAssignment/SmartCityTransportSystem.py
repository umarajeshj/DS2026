class Vehicle:
    def __init__(self,vehicle_id):
        self.vehicle_id = vehicle_id
        # print(f"Vehicle id :",vehicle_id)

    def calculate_fare(self,**args):
        print(f"Calculate fare :")

class Bus(Vehicle):
    def calculate_fare(self, **args):
        return 10.0

class Taxi(Vehicle):
    def calculate_fare(self,distance,isPeak=False):
        ticketPrice = distance * 10.0
        if isPeak:
            ticketPrice = ticketPrice * 2.0
        return ticketPrice

class Metro(Vehicle):
     def calculate_fare(self,zones,isPeak=False):
        ticketPrice = zones * 10.0
        if isPeak:
            ticketPrice = ticketPrice * 1.2
        return ticketPrice

def display_ticketPrice(vehicles):
    for vehicle,args in vehicles:
        fare = vehicle.calculate_fare(**args)
        print(f"{vehicle.__class__.__name__}({vehicle.vehicle_id}):Rs.{fare:.2f}")

vehicles = [
    (Bus("Bus01"), {}),
    (Taxi("Taxi01"), {"distance": 10, "isPeak": False}),
    (Metro("Metro01"), {"zones": 3, "isPeak": True})
]

display_ticketPrice(vehicles)
