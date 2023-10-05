motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() #метод .pop позволяет вытянуть из списка содержимое и позволяет с ним работать
print(motorcycles)
print(popped_motorcycle)


motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(motorcycles)
print(f"{last_owned.title()}, был последним мотоциклом который я купил.")


motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0) # При установке числа в () будет использоваться содержимое, находящееся в этом месте списка
print(f'{first_owned.title()}, был первым мотоциклом который я купил.')
#del и .pop сильно отличаются, но при этом они удаляют содержимое из списка, только del удаляет без возможности взаимодействия, когда .pop позволяет использовать убранный элемент