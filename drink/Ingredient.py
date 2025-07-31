class Ingredient():
    def toString(self):
        print("Ingredient: " + str(self.amount) + " " + self.measurement + " " + self.name)
        print("Ingredient is a type of " + self.type)

    def toInsert(self, last_row):
        data = (last_row, self.amount, self.measurement, self.name, self.type)
        return data
    
    def __init__(self, amount, measurement, name, type):
        self.amount = amount
        self.measurement = measurement
        self.name = name
        self.type = type

