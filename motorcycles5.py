motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') #метод .remove позволяет зная значение убирает его, позволяя работать с ним
print(motorcycles)
print('------')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()}, слишком дорогая для меня")