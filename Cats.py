# Cat class

# Hidden Attributes
# Mood
# Hunger
# Energy

# Methods
# Sleep
# Play
# Feed

# Hidden Method
# Meow

# class Cat:
#
#     def __init__(self):
#         self._Mood = 5
#         self._Hunger = 5
#         self._Energy = 5
#         self._Meow()
#         self.action = input("What is the cat doing? Sleep/Play/Feed \n").upper()
#         self.sleep()
#         self.play()
#         self.feed()
#
#
#     def sleep(self):
#         if self.action == "SLEEP":
#             self._Energy += 5
#             self._Mood += 4
#             self._Meow()
#
#
#     def play(self):
#         if self.action == "PLAY":
#             self._Energy -= 4
#             self._Mood += 3
#             self._Hunger += 3
#             self._Meow()
#
#
#     def feed(self):
#         if self.action == "FEED":
#             self._Hunger -= 4
#             self._Mood += 2
#             self._Energy += 3
#             self._Meow()
#         print("Energy:", self._Energy, "Mood:", self._Mood, "Hunger:", self._Hunger)
#
#     def _Meow(self):
#         print("Meow")
#
# my_cat = Cat()

# class Animal:
#     def __init__(self):
#         self.hunger = 5
#         self.name = input("name?")
#         self.colour = input("colours")
#
#     def breathe (self):
#         print("Breathing in...")
#         print("Breathing out...")
#         self.hunger += 1
#
#     def eat(self):
#         print("nom nom nom")
#         self._hunger = 0
#
# class Mammal(Animal):
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#
#     def give_birth(self):
#         print("I make children not eggs")
#
#
# class Dog(Mammal):
#
#     def __init__(self, name, colour):
#         super().__init__(name, colour)
#
#     def wag_tail(self):
#         print("Swish swish")
#         self.hunger += 1
#
# # class Poodle(Dog):
# #     def fluff(self):
# #         print("I am fluffy")
# #         self.hunger += 1
#
# class Bat(Mammal):
#     def __init__(self, name, colour):
#         super().__init__(name, colour)
#         self.legs = 2
#
# class Platypus(Mammal):
#     def __init__(self, name, colour):
#         super().__init__(name, colour)
#
# perry = Platypus("perry", "teal")
#
# perry.give_birth()



