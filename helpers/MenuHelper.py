class MenuHelper():
    @staticmethod
    def displayMainMenu():
        menuOptions = ["Please select a menu option from below:","1: Add a drink to the database","2: Edit a drink in the database","3: Remove a drink in the database","4: View a drink","5: Add from File","6: Add to remote database","0: Exit"]
        for i in menuOptions:
            print(i + "\r")    

    @staticmethod
    def displayMeasurements():
        measurements = ["Ounce(s)", "ML", "each","dash(s)"]
        measurementCount = 1
        for measurement in measurements:
            print(str(measurementCount) + ": " + measurement)
            measurementCount+=1

    @staticmethod
    def displaySources():
        sources = ["Anime", "Books", "Cartoons", "Comic Books", "Games", "Movies", "TV", "Video Games"]
        sourceCount = 1
        for source in (sources):
            print(str(sourceCount) + ": " + source)
            sourceCount+=1

