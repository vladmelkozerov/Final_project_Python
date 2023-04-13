class Menu():
    """Модель меню в ресторане"""
    def __init__(self,content):

        self.content = content
    def display(self):
        """Вывод меню"""
        print(f" Меню таверны на 12 04 23 ")
        for key,value in self.content.items():
            print(f"{key}  {value.name:15} Цена {value.price} руб.")
