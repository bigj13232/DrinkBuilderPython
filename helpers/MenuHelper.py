class MenuHelper():
    @staticmethod
    def displayMainMenu():
        menuOptions = ["Please select a menu option from below:","1: Add a drink to the database","2: Edit a drink in the database","3: Remove a drink in the database","4: View a drink","0: Exit"]
        for i in menuOptions:
            print(i + "\n")
