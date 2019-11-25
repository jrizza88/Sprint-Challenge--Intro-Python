# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class - Vehicle

class Vehicle:
    # base class 
    pass

class GroundVehicle(Vehicle):
    # secondary class (parent is Vehicle)
    pass

class Car(GroundVehicle):
    # third level class Grandparent Vehicle, parent is GroundVehicle
    pass

class Motorcycle(GroundVehicle):
    # third level class Grandparent Vehicle, parent is GroundVehicle
    pass

class FlightVehicle(Vehicle):
    # secondary class (parent is Vehicle)
    pass

class Starship(FlightVehicle):
    # third level class Grandparent Vehicle, parent is FlightVehicle
    pass

class Airplane(FlightVehicle):
        # third level class Grandparent Vehicle, parent is FlightVehicle
    pass


# class Vehicle:
#     def __init__(self, vehicle):
#         self.vehicle = vehicle

#     def __str__(self):
#         return f'the Vehicle name is {self.vehicle}.'


# class FlightVehicle(Vehicle):
#     def __init__(self, vehicle, flight_vehicle):
#         super().__init__(vehicle)
#         self.flight_vehicle = flight_vehicle

#     def __str__(self):
#         return f'Class FlightVehicle vehicle: {self.vehicle}; flight_vehicle: {self.flight_vehicle}.'

# class Starship(FlightVehicle):
#     def __init__(self, vehicle, flight_vehicle, starship):
#         super().__init__(vehicle, flight_vehicle)
#         self.starship = starship

#     def __str__(self):
#         return f'Class Starship vehicle: {self.vehicle}; \n flight_vehicle: {self.flight_vehicle}, \n starship: {self.starship}.'
    
# class Airplane(FlightVehicle):
#     def __init__(self, vehicle, flight_vehicle, airplane):
#         super().__init__(vehicle, flight_vehicle)
#         self.airplane = airplane

#     def __str__(self):
#         return f'Class Airplane vehicle: {self.vehicle}; \n flight_vehicle: {self.flight_vehicle}, \n airplane: {self.airplane}.'


# class GroundVehicle(Vehicle):
#     def __init__(self, vehicle, ground_vehicle):
#         super().__init__(vehicle)
#         self.ground_vehicle = ground_vehicle

#     def __str__(self):
#         return f'Class GroundVehicle vehicle: {self.vehicle}, \n ground_vehicle: {self.vehicle}'

# class Car(GroundVehicle):
#     def __init__(self, vehicle, ground_vehicle, car):
#         super().__init__(vehicle, ground_vehicle)
#         self.car = car

#     def __str__(self):
#         return f'Class Car vehicle: {self.vehicle}, \n ground_vehicle: {self.vehicle} \n car: {self.car}'

# class Motorcycle(GroundVehicle):
#     def __init__(self, vehicle, ground_vehicle, motorcycle):
#         super().__init__(vehicle, ground_vehicle)
#         self.motorcycle = motorcycle

#     def __str__(self):
#         return f'Class Motorcycle vehicle: {self.vehicle}, \n ground_vehicle: {self.vehicle} \n motorcycle: {self.motorcycle}'