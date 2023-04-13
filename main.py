from Dish import Dish
from Drink import Drink
from Menu import Menu
Dish1 = Dish("Лапша",150,15,200,"Да")
Dish2 = Dish("Расстегай",800,45,500,"Нет")
Dish3 = Dish("Буйабес",1400,90,400,"Да")
Drink1 = Drink("Cбитень",150,1,200,"Да")
Drink2 = Drink("Квас",100,1,200,"Нет")
Drink3 = Drink("Кофий",350,5,200,"Нет")
content = {1:Dish1,2:Dish2,3:Dish3,4:Drink1,5:Drink2,6:Drink3}
Menu1 = Menu(content)
Menu1.display()
choice = int(input("Для выбора блюда введите его номер: "))
print(f"Время подачи позиции меню {Menu1.content[choice].name} составит {Menu1.content[choice].serving_time} минут (ы)")
next = int(input("Для подтверждения заказа введите 1, для отмены введите 2: "))
if (next == 1):
    Menu1.content[choice].order()
    if isinstance(Menu1.content[choice],Dish):
        print(f"Заказ на блюдо передан на кухню, идет приготовление...")
        print(f"Информация о блюде. Калорийность: {Menu1.content[choice].nutritional_value} ккал, "
              f"Вегетарианское: {Menu1.content[choice].vegeterian}")
    else:
        print(f"Заказ на напиток передан в бар, идет приготовление...")
        print(f"Информация о напитке. Объем: {Menu1.content[choice].volume} мл, "
              f"Алкогольный: {Menu1.content[choice].alcohol}")
    Menu1.content[choice].serve()
    Menu1.content[choice].bill()
else:
    Menu1.content[choice].refuse()





