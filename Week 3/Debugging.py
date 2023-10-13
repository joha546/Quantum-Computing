'''Problem 1:
Debug the code shown below.
x = "17"
y = "3"
print(x*y)
'''

#Code:
x = 17
y = 3
print(x*y)

'''Problem 2:
Debug the code shown below.
my_list = [3, 1, 4, 1]
print(my_list[4])
'''
#Code:
my_list = [3, 1, 4, 1]
print(my_list[3])

'''Problem 3:
Debug the code shown below.
oak.set_light(6)
oak.set_water(8)
oak.grow()
'''
#Code:
class Plant:
    def __init__(self, health, water, light):
        self.health = health
        self.water = water
        self.light = light

    def check_health(self):
        return self.health

    def set_water(self, amount):
        self.water = amount

    def set_light(self, level):
        self.light = level

    def grow(self):
        if self.water >= 5 and self.light >= 5:
            self.health += 1
            self.water -= 5
            self.light -= 5
oak = Plant(health=8, water=8, light=8)
initial_health = oak.check_health()
print("Initial health of the oak plant:", initial_health)

oak.set_light(6)
oak.set_water(8)

oak.grow()
updated_health = oak.check_health()
print("Updated health of the oak plant:", updated_health)
