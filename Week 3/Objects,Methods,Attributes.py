'''Problem 1:
Create a baby object and set its age to 1. Then print out its "age" attribute.
'''
# Code:

class Baby:
    def __init__(self, age):
        self.age = age

my_baby = Baby(1)
print("The baby's age is:", my_baby.age)

''' Problem 2:
Print out the baby's hunger and mood attributes.
'''
# Code:

class Baby:
    def __init__(self, age, hunger, mood):
        self.age = age
        self.hunger = hunger
        self.mood = mood
my_baby = Baby(age=1, hunger="hungry", mood="happy")

print("Baby's age:", my_baby.age)
print("Baby's hunger:", my_baby.hunger)
print("Baby's mood:", my_baby.mood)

'''Problem 3:
Now, use the baby's feed and play methods. Then print out its hunger and mood attributes once again.
'''
#Code:
# COMPLETE THIS CODE
class Baby:
    def __init__(self, age, hunger, mood):
        self.age = age
        self.hunger = hunger
        self.mood = mood
    def feed(self):
        if self.hunger == "hungry":
            self.hunger = "full"
        else:
            print("The baby is not hungry.")
    def play(self):
        if self.mood == "happy":
            self.mood = "sad"
        else:
            print("The baby doesn't want to play right now.")
my_baby = Baby(age=1, hunger="hungry", mood="happy")
print("Baby's age:", my_baby.age)
print("Baby's hunger:", my_baby.hunger)
print("Baby's mood:", my_baby.mood)
my_baby.feed()
my_baby.play()
print("Baby's age:", my_baby.age)
print("Baby's hunger:", my_baby.hunger)
print("Baby's mood:", my_baby.mood)


''' Problem 4:
Create a plant object using its corresponding function, and use the check_health method to measure the plant's health.
'''

#Code:
# COMPLETE CODE
class Plant:
    def __init__(self, health):
        self.health = health

    def check_health(self):
        return self.health
my_plant = Plant(health=8)
plant_health = my_plant.check_health()
print("Plant's health:", plant_health)

'''Problem 5:
Using the necessary methods and attributes, get your plant to grow a bit.

Hint: Read through the plant class to see if there is a way to give it the perfect amount of water and light without 
guessing and checking.'''
#Code:
# COMPLETE THIS CODE
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
my_plant = Plant(health=8, water=8, light=8)
my_plant.set_water(10)
my_plant.set_light(10)
my_plant.grow()
plant_health = my_plant.check_health()
print("Plant's health:", plant_health)
