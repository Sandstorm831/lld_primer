from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class VehicleType(Enum):
    Car = 1
    Truck = 2
    Bike = 3


class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.type = vehicle_type
        self.license_plate = license_plate

    def getVehicleType(self):
        return self.vehicle_type


class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.Car)


class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.Truck)


class Bike(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.Bike)


class Spot():
    def __init__(self, spot_number: int):
        self.spot = spot_number
        self.vehicleType: VehicleType = VehicleType.Car
        self.occupied: bool = False

    def canParkVehicle(self, vehicle: Vehicle):
        return vehicle.type == self.vehicleType.type and not self.occupied

    def parkVehicle(self, vehicle: Vehicle):
        if not self.canParkVehicle(vehicle):
            return False
        self.occupied = True
        return True

    def releaseVehicle(self, vehicle: Vehicle):
        if self.occupied and self.vehicleType.type == vehicle.type:
            self.occupied = False
            return True
        return False

    def isOccupied(self):
        return self.occupied

    def vehicleType(self):
        return self.vehicleType.type

    def getSpotNumber(self):
        return self.spot


class ParkingLevel():
    def __init__(self, levelNum: int, numSpots: int):
        self.level = levelNum
        self.spots = numSpots
        self.parkingSpots: List[Spot] = [Spot(i) for i in range(numSpots)]

    def getParkingSpots():
        # code to get total number
        pass

    def parkVehicle(vehicle: Vehicle):
        # code
        pass

    def releaseVehicle(vehicle: Vehicle):
        # code
        pass


class ParkingLot():
    __theLot = None

    def __new__(cls):
        if not cls.__theLot:
            print("creating the object")
            cls.__theLot = super(ParkingLot, cls).__new__(cls)
        return cls.__theLot

    def __init__(self, levels: int):
        if not hasattr(self, 'Lot'):
            self.Lot: List[ParkingLevel] = [
                ParkingLevel(i, 10) for i in range(levels)]
            print("initializing singleton with levels")

    @staticmethod
    def getInstnce():
        if ParkingLot.__theLot is None:
            ParkingLot()
        return ParkingLot.__theLot

    def getParkingSpots(self):
        # code
        pass

    def parkVehicle(self, vehicle: Vehicle):
        # code
        pass

    def releaseVehicle(self, vehicle: Vehicle):
        # code
        pass
