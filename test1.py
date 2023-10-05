name = ['Артур', 'Максим', 'Млада', 'Юрий', 'Евгений']
busy_guest = name.pop()
name.append('Витя')
print(f'{busy_guest.title()} не сможет прийдти, так как занят.')
print('Список гостей был расширен')
name.insert(0, 'Ольга')
name.insert(0, 'Роман')
name.append('Кристина')
message = f"Привет {name[0].title()}, я приглашаю тебя на вечеринку завтра в 8, надеюсь на то что ты прийдёшь!"
print(message)
message = f"Привет {name[1].title()}, я приглашаю тебя на вечеринку завтра в 8, надеюсь на то что ты прийдёшь!"
print(message)
message = f"Привет {name[2].title()}, я приглашаю тебя на вечеринку завтра в 8, надеюсь на то что ты прийдёшь!"
print(message)
message = f"Привет {name[3].title()}, я приглашаю тебя на вечеринку завтра в 8, надеюсь на то что ты прийдёшь!"
print(message)
message = f"Привет {name[4].title()}, я приглашаю тебя на вечеринку завтра в 8, надеюсь на то что ты прийдёшь!"
print(message)
message = f"Привет {name[5].title()}, я приглашаю тебя на вечеринку завтра в 8, надеюсь на то что ты прийдёшь!"
print(message)
message = f"Привет {name[6].title()}, я приглашаю тебя на вечеринку завтра в 8, надеюсь на то что ты прийдёшь!"
print(message)
message = f"Привет {name[7].title()}, я приглашаю тебя на вечеринку завтра в 8, надеюсь на то что ты прийдёшь!"
print(message)
sorry = name.pop()
sorry_message = f"Прости, {sorry.title()}, я пригласил тебя, но так вышло что места не хватит, я сожалею об отмене пришлашения :c."
print(sorry_message)
sorry = name.pop()
sorry_message = f"Прости, {sorry.title()}, я пригласил тебя, но так вышло что места не хватит, я сожалею об отмене пришлашения :c."
print(sorry_message)
sorry = name.pop()
sorry_message = f"Прости, {sorry.title()}, я пригласил тебя, но так вышло что места не хватит, я сожалею об отмене пришлашения :c."
print(sorry_message)
sorry = name.pop()
sorry_message = f"Прости, {sorry.title()}, я пригласил тебя, но так вышло что места не хватит, я сожалею об отмене пришлашения :c."
print(sorry_message)
sorry = name.pop()
sorry_message = f"Прости, {sorry.title()}, я пригласил тебя, но так вышло что места не хватит, я сожалею об отмене пришлашения :c."
print(sorry_message)
sorry = name.pop()
sorry_message = f"Прости, {sorry.title()}, я пригласил тебя, но так вышло что места не хватит, я сожалею об отмене пришлашения :c."
print(sorry_message)
message2 = f'Привет, {name[0].title()}, ранее приглашениее всё ещё в силе!'
print(message2)
message2 = f'Привет, {name[1].title()}, ранее приглашениее всё ещё в силе!'
print(message2)
del name[0]
del name[0]
print(name) #Список гостей, который изменялся со временем. Юрий 04.10.23