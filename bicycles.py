bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #[] <- Задают список
print(bicycles) #Выводит переменную бикукле
print(bicycles[0]) #[0] <- обращение к элементу, начинается с 0
print(bicycles[0].title()) # Выводит отформатированный trek в Trek
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) #[-1] всегда возвращает последний элемент в списке, [-2] вернет предпоследний и т.д.

message = f"Мой первый велосипед был {bicycles[0].title()}"
print(message)