from Menu_position import Menu_position
class Dish (Menu_position):
    def __init__(self,name,price,serving_time,weight,vegeterian):
        super().__init__(name,price,serving_time)
        self.nutritional_value = weight
        self.vegeterian = vegeterian
