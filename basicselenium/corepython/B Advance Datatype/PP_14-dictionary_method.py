"""
Dictionary Methods
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}  # key = make,model,year && value = bmw,550i,2016
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}} #

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())

car_copy = car.copy()
print(car_copy)

print(car.pop('model')) # means take out==> model: 550i
print(car)