from drink.Ingredient import Ingredient
from drink.Ingredient import Ingredient
class Drink():
    def toString(self):
        print("Drink Name is: " + self.name)
        print("Drink Source is: " + self.source)
        print("Drink origin is: " + self.origin)
        print("Drink Directions are: \n" + self.directions)
        print("Is it a mocktail? " + str(self.isMocktail))

    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)

    def listIngredients(self):
        for ingredient in self.ingredients:
            ingredient.toString()

    #Constructor
    def __init__(self, name, source, origin, directions, isMocktail):
        self.name = name
        self.source = source
        self.origin = origin
        self.directions = directions
        self.isMocktail = isMocktail
        self.ingredients = []
