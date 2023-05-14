class Food:
    def __init__(self, name, foodType):
        self.name = name
        self.type = foodType
    
    def yourFoodInfo(self):
        print("Today's meal is", self.name, "and it is of type", self.type)

mealOne = Food("red velvet cake", "dessert")
mealOne.yourFoodInfo()