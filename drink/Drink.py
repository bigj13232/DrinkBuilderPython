class Drink():
    def toString(self):
        print("Drink Name is: " + self.name)
        print("Drink Source is: " + self.source)
        print("Drink origin is: " + self.origin)
        print("Drink Directions are: \n" + self.directions)
        print("Is it a mocktail? " + str(self.isMocktail))

    
    #Constructor
    def __init__(self, name, source, origin, directions, isMocktail):
        self.name = name
        self.source = source
        self.origin = origin
        self.directions = directions
        self.isMocktail = isMocktail
