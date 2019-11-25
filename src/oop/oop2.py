# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # TODO
    def __str__(self):
        output = f'Groundvehicle Class - number of wheels: {self.num_wheels}.'
        return output

    def drive(self):
        drive = "vroooom"
        print(drive)
        return f'{drive}'


        


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)

    def __str__(self):
        output = f'Motorcycle Class - number of wheels: {self.num_wheels}.'
        return output
# TODO
    def drive(self):
        drive = "BRAAAP!!"
        print(drive)
        return f'{drive}'

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
for d in vehicles:
    print(d.drive())
# TODO
