# store class that has a name and a categories
class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"{self.name}\n"
        for i, c in enumerate(self.categories):
            output += "   " + str(i + 1) + ": " + c + "\n"
        
        output += "   " + str(i + 2) + ": Exit"
        return output

s = Store("Books n thingz", ["Fiction", "Non Fiction", "Golf Balls", "Some other Cat"])

print(s) # self.__repr__() => self.__str__()

