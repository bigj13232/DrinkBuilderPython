from drink.Ingredient import Ingredient
from drink.Ingredient import Ingredient
class Drink():
    def toString(self):
        print("Drink Name is: \n" + self.name)
        print("Drink Source is: \n" + self.source)
        print("Drink origin is: \n" + self.origin)
        print("Drink Directions are: \n" + self.directions)
        print("Drink Source is: \n" + self.drinkWebsite)
        print("Is it a mocktail? " + str(self.isMocktail))

    def toInsert(self):
        data = (self.name, self.source, self.origin, self.directions, self.isMocktail, self.drinkWebsite, self.drinkWebsiteURL)
        return data 

    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)

    def listIngredients(self):
        for ingredient in self.ingredients:
            ingredient.toString()

    #Constructor
    def __init__(self, name, source, origin, directions, isMocktail, drinkWebsite,drinkWebsiteURL):
        self.name = name
        self.source = source
        self.origin = origin
        self.directions = directions
        self.isMocktail = isMocktail
        self.ingredients = []
        self.drinkWebsite = drinkWebsite
        self.drinkWebsiteURL = drinkWebsiteURL
