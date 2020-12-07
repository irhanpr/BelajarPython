class Car (object):
    def __init__(self, make, model, color):
        self.make = make;
        self.model = model;
        self.color = color;
        
myCar = Car("Honda", "Accord", "Blue")
print(myCar.make)
print(myCar.model)
print(myCar.color)