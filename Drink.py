from Menu_position import Menu_position


class Drink(Menu_position):
    def __init__(self, name, price, serving_time, volume, alcohol):
        super().__init__(name, price, serving_time)
        self.volume = volume
        self.name = name
        self.alcohol = alcohol


