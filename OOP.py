# Don't
# Repeat
# Yourself

# def print_something():
#     print("Something!")
#
# print_something()
# print_something()
# print_something()

# def print_something_multiple(some_string, number_of_times):
#     string_to_print = some_string * number_of_times
#     print(string_to_print)
#
# print_something_multiple("WooHoo! ", 5)
#
# def repeat_string(string_to_repeat="WooHoo! ", number_of_repeats=3):
#     string_to_return = string_to_repeat * number_of_repeats
#     return string_to_return
#;
# print(repeat_string(number_of_repeats=5))
#
# my_string = repeat_string("Hello!", 5)
# print(my_string)
#
# def addition(first_to_add, second_to_add):
#     return first_to_add + second_to_add


# def find_product(*multiargs):
#     if len(multiargs) < 1:
#         return None
#     else:
#         chose_num = 1
#         for num in multiargs:
#             multiple = chose_num * num
#         return multiple
#
#
# print(find_product(1 ,2, 3, 4, 5))

# def repeat_string(string_to_repeat: str, number_of_repeats: int) -> str:
#     string_to_return = string_to_repeat * number_of_repeats
#     return string_to_return
# repeat_string("woohoo", 5).upper

#CLASSES

# class GoodDog:
#     animal_type = "canine" # Attribute (Variable)
#
#     def bark(self): # Method (Function)
#         return "Woof!"
#
#
# fluffy = GoodDog()
# print(fluffy.animal_type)
# print(fluffy.bark())
#
# fido = GoodDog()
# lassie = GoodDog()
#
# fido.animal_type = "bird"
# print(lassie.bark())
#
# print(lassie.animal_type)
#
# print("----------Horrible Curse-----------")
# GoodDog.animal_type = "arachnid"
# print(lassie.animal_type)
# print(fido.animal_type)
# print(fluffy.animal_type)

# class Dog:
#     animal_kind = "canine"
#     def __init__(self): #Initilisation
#         self.name = "Jimmy"
#         self.legs = 4
#         self.animal_kind = "canine"
#
#     def bark(self):
#         return("Woof!")

# big_dog = Dog()
# small_dog = Dog()
#
# print(big_dog.name)
# print(small_dog.legs)
# print(big_dog.animal_kind)
#
# print("------HORRIBLE CURSE------")
# Dog.animal_kind = "arachnids"
# Dog.legs = 8
#
# print(big_dog.animal_kind)
# print(big_dog.legs)

# class Dog:
#     animal_kind = "canine"
#
#     def __init__(self, name: str, size: str):  # Initilisation
#         self.name = name
#         self.legs = 4
#         self.animal_kind = "canine"
#         self.size = size
#         self.__secret = "I can't eat chocolate"  # Private variable
#
#     def bark(self):
#         return("Woof!")
#
#     def nameCall(self):
#         return(f"I'm a Dog called {self.name}")
#
#     def reveal_secret(self): #GETTER
#         return self.__secret
#
#     def set_secret(self, secret):  # SETTER
#         self.__secret = secret
#
#
# new_dog = Dog("Pablo", "Small")
#
# print(new_dog.reveal_secret())
# new_dog.set_secret("I hid my bone")
# print(new_dog.reveal_secret())

# class Car:
#
#     def __init__(self, model: str, doors: int, make: str):
#         self.model = model
#         self.doors = doors
#         self.make = make
#         self.maxSpeed = 200
#         self._start_speed = 0
#         self._acceleration = 0
#         self._distance = 0
#
#     def speed(self, speed, acceleration, distance):
#         self._start_speed = speed
#         self._acceleration = acceleration
#         self._distance = distance
#         final_speed = self._start_speed + (self._distance * self._acceleration)
#         if self.maxSpeed < final_speed or final_speed < 0:
#             print("Cars can not accelerate to this speed")
#         else:
#             return final_speed
#
# car1 = Car("Model", 5, "Make")
# print(car1.speed(15, 200, ))

import random as rn
print(rn.randint(1, 100))
print(rn.random())

#from page import class
list = [1, 2, 6, 9, 12, 11, 14]
