class Menu_position():
    """Модель блюда в ресторане"""
    def __init__(self,name,price,serving_time):
        self.name = name
        self.price = price
        self.serving_time = serving_time
    def order(self):
        """Заказ из меню"""
        print(f"Заказ на {self.name} принят, стоимость составляет {self.price} рублей")
    def refuse(self):
        """Отказ от заказа"""
        print(f"Заказ  {self.name} отменен")
    def bill(self):
        """Оплата заказа"""
        print(f"Заказ {self.name} на сумму {self.price} рублей успешно оплачен")
    def serve(self):
        """Подача заказа"""
        print(f"Заказ {self.name} подан")







